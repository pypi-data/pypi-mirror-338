#!/usr/bin/env python3

"""
Generates WUI building dataset with fire risk attributes and fire modeling input rasters for a given AOI.

Process includes:
1. Processing building footprints and calculating spatial metrics
2. Assigning fire-related attributes to buildings
3. Creating gridded raster outputs for fire modeling
4. Generating vector building footprint dataset with attributes

Outputs:
- GeoJSON of building footprints with fire risk-related attributes
- Raster layers for wildland-urban fire modeling (building separation, footprint fraction, fuel models, etc.)
- Modified FBFM40 fuel model raster distinguishing buildings from roadways (saved as fbfm40b.tif)

To do:
    - Add user option to specify input AOI other than raster
    - Produce SSD rasters for N/E/S/W
    - Add user option to specify fire year (for hindcasting purposes) and adjust building footprints
        to reflect pre-fire conditions.
"""

import os
import argparse
from datetime import datetime

import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.features import rasterize
from shapely.geometry import box

from firedx.utils import aoi_to_epsg4326, read_data_as_gdf
import firedx.footprints as footprints
import firedx.attributes as attributes
from firedx.bldg_fuel_models import assign_bldgfm
from firedx.modify_fbfm import raster_cells_to_polygons, modify_fm


def _calculate_cell_metrics(bldg_ids, dict_lookup, calculation_type="average"):
    """Calculates specified metric from building IDs and value lookup."""
    values = [dict_lookup[id] for id in bldg_ids]

    if calculation_type == "average":
        return sum(values) / len(values) if values else 0
    elif calculation_type == "minimum":
        if not values:
            raise ValueError("Cannot calculate minimum of empty list")
        return min(values)
    else:
        raise ValueError(
            f"Invalid calculation type: {calculation_type}. Use 'average' or 'minimum'."
        )


def _calculate_intersection_metrics(buildings_gdf, grid_geom, bldg_ids):
    """Calculates footprint fractions and dominant fuel model for grid cell."""
    total_footprint_area = 0.0
    fire_resistant_area = 0.0
    largest_area = 0.0
    dominant_fm = -9999

    for bldg_id in bldg_ids:
        bldg = buildings_gdf[buildings_gdf["BLDG_ID"] == bldg_id].iloc[0]
        intersect = bldg.geometry.intersection(grid_geom)

        if not intersect.is_empty:
            area = intersect.area
            total_footprint_area += area

            if bldg.fire_resistance in ("rated", "protected"):
                fire_resistant_area += area

            if area > largest_area:
                largest_area = area
                dominant_fm = bldg.BLDG_FUEL_MODEL

    footprint_frac = (
        total_footprint_area / grid_geom.area if grid_geom.area > 0 else 0.0
    )
    fire_resist_frac = (
        fire_resistant_area / total_footprint_area if total_footprint_area > 0 else 0.0
    )

    return footprint_frac, dominant_fm, fire_resist_frac


def assign_raster_values(aoi_grid, buildings_gdf):
    """Calculates grid cell metrics from building footprints."""

    buildings_gdf["BLDG_ID"] = buildings_gdf.index

    if "BLDG_AREA_m2" not in buildings_gdf.columns:
        buildings_gdf = footprints.calculate_bldg_metrics(buildings_gdf)

    bldgs_gridded_data = (
        aoi_grid.sjoin(
            buildings_gdf[["BLDG_ID", "geometry"]], how="inner", predicate="intersects"
        )
        .groupby("geometry")["BLDG_ID"]
        .agg(list)
        .reset_index()
    )

    # Create lookup dictionaries for cell metrics
    separation_lookup = dict(
        buildings_gdf[["BLDG_ID", "BLDG_SEPARATION_DIST_MIN"]].values
    )
    area_lookup = dict(buildings_gdf[["BLDG_ID", "BLDG_AREA_m2"]].values)
    height_lookup = dict(buildings_gdf[["BLDG_ID", "BLDG_HEIGHT"]].values)

    bldgs_gridded_data["BLDG_SSD_MIN"] = bldgs_gridded_data["BLDG_ID"].apply(
        lambda x: _calculate_cell_metrics(x, separation_lookup, "minimum")
    )

    bldgs_gridded_data["BLDG_AREA_AVG_m2"] = bldgs_gridded_data["BLDG_ID"].apply(
        lambda x: _calculate_cell_metrics(x, area_lookup, "average")
    )

    bldgs_gridded_data["BLDG_AREA_AVG_m"] = np.sqrt(
        bldgs_gridded_data["BLDG_AREA_AVG_m2"]
    ).round(3)

    bldgs_gridded_data["BLDG_HEIGHT_AVG"] = bldgs_gridded_data["BLDG_ID"].apply(
        lambda x: _calculate_cell_metrics(x, height_lookup, "average")
    )

    intersect_metrics = bldgs_gridded_data.apply(
        lambda row: _calculate_intersection_metrics(
            buildings_gdf, row.geometry, row.BLDG_ID
        ),
        axis=1,
    )

    bldgs_gridded_data["BLDG_FOOTPRINT_FRAC"] = intersect_metrics.apply(lambda x: x[0])
    bldgs_gridded_data["BLDG_FUEL_MODEL"] = intersect_metrics.apply(lambda x: x[1])
    bldgs_gridded_data["BLDG_NONBURNABLE_FRAC"] = intersect_metrics.apply(
        lambda x: x[2]
    )

    bldgs_gridded_data["BLDG_FUEL_MODEL"] = (
        pd.to_numeric(bldgs_gridded_data["BLDG_FUEL_MODEL"], errors="coerce")
        .fillna(-9999)
        .astype(np.int16)
    )

    return bldgs_gridded_data


def save_rasters(gridded_data, raster_meta, output_dir):
    """Saves calculated metrics as GeoTIFF rasters.

    Args:
        gridded_data: GeoDataFrame with metrics
        raster_meta: Dictionary with 'crs', 'transform', and 'shape'
        output_dir: Path to save output files
    """
    raster_specs = [
        {"filename": "ssd_min.tif", "column": "BLDG_SSD_MIN", "dtype": np.float32},
        # {'filename': 'ssd_N.tif', 'column': 'BLDG_SSD_MIN_N', 'dtype': np.float32},
        # {'filename': 'ssd_E.tif', 'column': 'BLDG_SSD_MIN_E', 'dtype': np.float32},
        # {'filename': 'ssd_S.tif', 'column': 'BLDG_SSD_MIN_S', 'dtype': np.float32},
        # {'filename': 'ssd_W.tif', 'column': 'BLDG_SSD_MIN_W', 'dtype': np.float32},
        {"filename": "baa_m2.tif", "column": "BLDG_AREA_AVG_m2", "dtype": np.float32},
        {"filename": "baa_m.tif", "column": "BLDG_AREA_AVG_m", "dtype": np.float32},
        {"filename": "bfm13.tif", "column": "BLDG_FUEL_MODEL", "dtype": np.int16},
        {"filename": "ff.tif", "column": "BLDG_FOOTPRINT_FRAC", "dtype": np.float32},
        {"filename": "nbf.tif", "column": "BLDG_NONBURNABLE_FRAC", "dtype": np.float32},
        {"filename": "bha.tif", "column": "BLDG_HEIGHT_AVG", "dtype": np.float32},
    ]

    no_data_value = -9999
    raster_profile_base = {"driver": "GTiff", "count": 1, "nodata": no_data_value}

    raster_profile = raster_profile_base.copy()
    raster_profile.update(
        {
            "height": raster_meta["shape"][0],
            "width": raster_meta["shape"][1],
            "crs": raster_meta["crs"],
            "transform": raster_meta["transform"],
        }
    )

    for spec in raster_specs:
        output_path = os.path.join(output_dir, spec["filename"])
        geometries = zip(gridded_data.geometry, gridded_data[spec["column"]])

        raster = rasterize(
            geometries,
            out_shape=raster_meta["shape"],
            transform=raster_meta["transform"],
            fill=no_data_value,
            dtype=spec["dtype"],
        )

        with rasterio.open(
            output_path, "w", **raster_profile, dtype=spec["dtype"]
        ) as dst:
            dst.write(raster, 1)
            dst.close()

        print(f"Created raster: {output_path}")


def main(fbfm40_path, save_buildings=True, footprints_in=None, output_dir=None):
    start_time = datetime.now()

    output_dir = output_dir or os.path.dirname(fbfm40_path)
    os.makedirs(output_dir, exist_ok=True)

    with rasterio.open(fbfm40_path) as src:
        raster_meta = {
            "bounds": src.bounds,
            "transform": src.transform,
            "shape": src.shape,
            "crs": src.crs,
            "resolution": src.res,
            "profile": src.profile,
        }
        fbfm40_data = src.read()

    if footprints_in:  # use existing footprints
        print(f"Reading building footprints from {footprints_in}...")
        buildings = read_data_as_gdf(footprints_in)
        buildings = buildings.to_crs(raster_meta["crs"])
    else:
        print("Fetching and processing building footprints...")
        aoi_geojson = aoi_to_epsg4326(
            raster_bounds=raster_meta["bounds"], raster_crs=raster_meta["crs"]
        )
        buildings = footprints.get_footprints(
            aoi_geojson,
            raster_meta["crs"],
            calculate_metrics_flag=True,
            save_file=False,
        )

    if "BLDG_FUEL_MODEL" in buildings.columns:
        print("Footprints already prepared for rasterization.")
    else:
        print("Joining building attributes...")
        buildings = attributes.join_to_footprints(
            buildings, aoi_geojson, raster_meta["crs"]
        )
        buildings = assign_bldgfm(buildings)

        if save_buildings:
            buildings.to_file(f"{output_dir}/buildings_data.geojson", driver="GeoJSON")
            print(
                f"Building footprints data saved to {output_dir}/buildings_data.geojson"
            )

    print("Creating gridded metrics...")
    grid_cells = raster_cells_to_polygons(
        fbfm40_data,
        raster_meta["crs"],
        raster_meta["resolution"],
        raster_meta["bounds"],
        target_value="all",
    )
    gridded_metrics = assign_raster_values(grid_cells, buildings)

    print("Saving rasters...")
    save_rasters(gridded_metrics, raster_meta, output_dir)

    print("Updating fuel models...")
    modify_fm(fbfm40_data, raster_meta["profile"], output_dir)

    duration = datetime.now() - start_time
    mins, secs = divmod(duration.seconds, 60)
    print(f"\nExecution time: {mins}m {secs}s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate WUI fire modeling datasets from the FBFM40 raster."
    )
    parser.add_argument("fbfm40_path", help="Path to the FBFM40 input raster")
    parser.add_argument(
        "--footprints_in",
        type=str,
        required=False,
        help="Path to existing building footprints file",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=False,
        help="Output directory (default: input raster directory)",
    )

    args = parser.parse_args()
    main(args.fbfm40_path, footprints_in=args.footprints_in, output_dir=args.output_dir)
