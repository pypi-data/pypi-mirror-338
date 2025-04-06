#!/usr/bin/env python3

import os
import warnings
import tempfile
import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed

import mercantile
import numpy as np
import pandas as pd
import geopandas as gpd
import shapely.geometry
import osmnx as ox
from tqdm import tqdm
#from tqdm.contrib.concurrent import process_map


def process_quad_key(quad_key, df, aoi_bbox, tmpdir):
    rows = df[df["QuadKey"] == quad_key]
    if rows.shape[0] == 1:
        url = rows.iloc[0]["Url"]

        try:
            df2 = pd.read_json(url, lines=True)
            df2["geometry"] = df2["geometry"].apply(shapely.geometry.shape)

            gdf = gpd.GeoDataFrame(df2, crs=4326)
            with tempfile.NamedTemporaryFile(
                suffix=".geojson", delete=False, dir=tmpdir
            ) as tmp_file:
                gdf.to_file(tmp_file.name, driver="GeoJSON")

            gdf_filtered = gpd.read_file(tmp_file.name)

            combined_rows = []
            for idx, row in enumerate(gdf_filtered.itertuples(), start=1):
                shape = row.geometry
                height = getattr(row, "properties", None)
                height_val = float(str(height)[12:15]) if height else None

                if aoi_bbox.contains(shape):
                    combined_rows.append(
                        {"geometry": shape, "height": height_val, "msid": idx}
                    )

            return combined_rows

        except Exception as e:
            print(f"Error processing QuadKey {quad_key}: {e}")
            return []

    elif rows.shape[0] > 1:
        print(f"Multiple rows found for QuadKey: {quad_key}")
        return []

    print(f"Skipping QuadKey not found in dataset: {quad_key}")
    return []


def ms_bldgs(aoi_bbox):
    """
    Fetches Microsoft Building Footprints for a given AOI and processes them in parallel.
    Adapted with modifications from: https://github.com/microsoft/GlobalMLBuildingFootprints/blob/main/examples/example_building_footprints.ipynb

    Parameters:
        aoi_bbox (Polygon): Area of interest.

    Returns:
        GeoDataFrame: A GeoDataFrame containing building footprints.
    """
    if not isinstance(aoi_bbox, (shapely.geometry.Polygon)):
        aoi_bbox = shapely.geometry.shape(aoi_bbox.get("geometry"))
    quad_keys = {
        int(mercantile.quadkey(tile))
        for tile in mercantile.tiles(*aoi_bbox.bounds, zooms=9)
    }
    print(f"The input area spans {len(quad_keys)} tiles: {quad_keys}")

    df = pd.read_csv(
        "https://minedbuildings.z5.web.core.windows.net/global-buildings/dataset-links.csv"
    )

    combined_rows = []

    with tempfile.TemporaryDirectory() as tmpdir:
        with ProcessPoolExecutor() as executor:
            futures = {
                executor.submit(
                    process_quad_key, quad_key, df, aoi_bbox, tmpdir
                ): quad_key
                for quad_key in quad_keys
            }

            for future in tqdm(
                as_completed(futures),
                total=len(futures),
                desc="Extracting footprints from tiles",
            ):
                result = future.result()
                if result:
                    combined_rows.extend(result)

    ms_footprints_gdf = gpd.GeoDataFrame(combined_rows, geometry="geometry", crs=4326)
    return ms_footprints_gdf


def osm_bldgs(aoi_bbox):
    if not isinstance(aoi_bbox, (shapely.geometry.Polygon)):
        aoi_bbox = shapely.geometry.shape(aoi_bbox.get("geometry"))
    osm_data = ox.features_from_polygon(aoi_bbox, tags={"building": True})
    osm_footprints_gdf = osm_data[
        osm_data.geom_type.isin(["Polygon", "MultiPolygon"])
    ].reset_index()[["id", "geometry"]]
    osm_footprints_gdf.rename(columns={"id": "osmid"}, inplace=True)
    return osm_footprints_gdf


# overture height not as complete as MS footprints
def overture_bldgs(aoi_bbox):
    if not isinstance(aoi_bbox, (shapely.geometry.Polygon)):
        aoi_bbox = shapely.geometry.shape(aoi_bbox.get("geometry"))

    command = [
        "overturemaps",
        "download",
        "--bbox",
        str(aoi_bbox.bounds)[1:-1],
        "-f",
        "geojson",
        "--type=building",
        "-o",
        "overture.geojson",
    ]
    subprocess.run(command)

    overture_footprints_gdf = gpd.read_file("overture.geojson")
    return overture_footprints_gdf


def calculate_bldg_metrics(footprints_gdf):
    """
    Calculates building area and minimum separation distance for each footprint in the GeoDataFrame.
    """
    if "BLDG_ID" not in footprints_gdf.columns:
        footprints_gdf["BLDG_ID"] = footprints_gdf.index + 1

    footprints_gdf["BLDG_AREA_m2"] = (
        footprints_gdf.geometry.area.round(3)
        if footprints_gdf.crs.axis_info[0].unit_name == "metre"
        else -9999
    )
    print(
        "Calculating footprint area, measuring separation distance..."
        if footprints_gdf["BLDG_AREA_m2"].iloc[0] != -9999
        else "CRS does not have units of meters. Building footprint area not calculated."
    )
    footprints_gdf["BLDG_AREA_m"] = np.sqrt(footprints_gdf["BLDG_AREA_m2"]).round(3)

    footprints_gdf["BLDG_SEPARATION_DIST_MIN"] = 999.0  # Initialize with large number

    spatial_index = footprints_gdf.sindex
    for index, polygon in tqdm(
        footprints_gdf["geometry"].items(), total=len(footprints_gdf)
    ):
        buffer_polygon = polygon.buffer(300)
        neighbors_idx = list(spatial_index.intersection(buffer_polygon.bounds))
        if index in neighbors_idx:
            neighbors_idx.remove(index)
        distances = footprints_gdf.iloc[neighbors_idx].distance(polygon)
        footprints_gdf.at[index, "BLDG_SEPARATION_DIST_MIN"] = (
            distances.min().round(3) if not distances.empty else 999.0
        )

    return footprints_gdf


def get_footprints(
    aoi_geojson, aoi_crs, calculate_metrics_flag=True, save_file=False, output_dir=None
):
    aoi_bbox = shapely.geometry.shape(aoi_geojson.get("geometry"))

    ms_footprints_gdf = ms_bldgs(aoi_bbox).set_crs("epsg:4326").drop(columns=["msid"])
    osm_footprints_gdf = (
        osm_bldgs(aoi_bbox).set_crs("epsg:4326").drop(columns=["osmid"])
    )

    intersections = gpd.sjoin(
        osm_footprints_gdf, ms_footprints_gdf, how="inner", predicate="intersects"
    )
    osm_gdf_filtered = osm_footprints_gdf.drop(intersections.index)

    footprints_joined = pd.concat(
        [ms_footprints_gdf, osm_gdf_filtered], ignore_index=True
    ).to_crs(aoi_crs)

    footprints_joined["BLDG_ID"] = footprints_joined.index + 1
    footprints_joined["height"] = pd.to_numeric(
        footprints_joined["height"].replace(-1, None), errors="coerce"
    )

    if calculate_metrics_flag:
        footprints_joined = calculate_bldg_metrics(footprints_joined)

    footprints_gdf = gpd.GeoDataFrame(footprints_joined, crs=aoi_crs)

    if save_file:
        if output_dir is None:
            warnings.warn(
                "Footprints file not saved. Please specify output directory.",
                UserWarning,
            )
        else:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)

            output_file = os.path.join(output_dir, "bldg_footprints.geojson")
            footprints_gdf.to_file(output_file, driver="GeoJSON")
            print(f"Saved footprints file to {output_file}")

    return footprints_gdf


if __name__ == "__main__":
    aoi_geojson = ""
    aoi_crs = ""
    footprints = get_footprints(aoi_geojson, aoi_crs)
