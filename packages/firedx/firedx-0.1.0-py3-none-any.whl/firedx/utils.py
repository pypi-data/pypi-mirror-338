import os
import sys
import json

import numpy as np
import pandas as pd
import geopandas as gpd
import fiona
import rasterio
from rasterio.warp import transform_bounds
from shapely.geometry import box
from rtree import index


## ********************************
## Geospatial & Geometry Helpers
## ********************************


def create_spatial_index(gdf):
    idx = index.Index()
    for i, geom in enumerate(gdf.geometry):
        if geom is not None:
            idx.insert(i, geom.bounds, obj=i)
    return idx


def add_lat_long_to_polygons(gdf):
    # gdf = gpd.read_file(input_file)
    # gdf = gdf.set_geometry('geometry')

    gdf["centroid"] = gdf.centroid
    gdf["LATITUDE"] = gdf["centroid"].y
    gdf["LONGITUDE"] = gdf["centroid"].x

    gdf = gdf.drop(columns="centroid")
    gdf_with_lat_long = gpd.GeoDataFrame(gdf)

    # df.to_csv(output_file, index=False)
    return gdf_with_lat_long


def aoi_to_epsg4326(raster_file=None, raster_bounds=None, raster_crs=None):
    """
    Convert the bounding box of a raster file or given bounds to EPSG:4326.

    Parameters:
        raster_file (str, optional): Path to the raster file representing the AOI.
        OR
        raster_bounds (tuple, optional): Bounding box (minx, miny, maxx, maxy).
        raster_crs (str or dict, optional): CRS of the raster bounds (e.g., 'EPSG:32633').

    Returns:
        dict: AOI geometry in EPSG:4326 as a GeoJSON-like dictionary.
    """

    if raster_file:
        with rasterio.open(raster_file) as src:
            bounds = src.bounds
            src_crs = src.crs
    elif raster_bounds and raster_crs:
        bounds = raster_bounds
        src_crs = raster_crs
    else:
        raise ValueError(
            "Either raster_file or (raster_bounds and raster_crs) must be provided."
        )

    dst_crs = "EPSG:4326"

    minx, miny, maxx, maxy = transform_bounds(
        src_crs, dst_crs, bounds.left, bounds.bottom, bounds.right, bounds.top
    )

    aoi_geometry = {
        "type": "Polygon",
        "coordinates": [
            [
                [minx, maxy],
                [minx, miny],
                [maxx, miny],
                [maxx, maxy], 
                [minx, maxy], 
            ]
        ],
    }

    aoi_geojson_epsg4326 = {
        "type": "Feature",
        "geometry": aoi_geometry,
        "properties": {},  # Empty properties for now
        "crs": {"type": "name", "properties": {"name": "EPSG:4326"}},
    }

    return aoi_geojson_epsg4326


def create_polygon_bbox(geojson_path: str):
    """
    Calculate the bounding box from a GeoJSON file.

    Parameters:
        geojson_path (str): Path to the GeoJSON file.

    Returns:
        list: Bounding box in the format [min_lon, min_lat, max_lon, max_lat].
    """
    with open(geojson_path, "r") as file:
        geojson_data = json.load(file)

    coordinates = geojson_data["features"][0]["geometry"]["coordinates"][0]

    min_lon = min(coord[0] for coord in coordinates)
    min_lat = min(coord[1] for coord in coordinates)
    max_lon = max(coord[0] for coord in coordinates)
    max_lat = max(coord[1] for coord in coordinates)

    return box(min_lon, min_lat, max_lon, max_lat)


def reproject_to_conus_albers(input_file: str, output_file: str):
    """
    Reproject a point dataset to EPSG:5070 (NAD83 / Conus Albers).

    Parameters:
        input_file (str): Path to the input file (shapefile, geojson, etc.).
        output_file (str): Path to save the reprojected file.

    Returns:
        gpd.GeoDataFrame: Reprojected GeoDataFrame.
    """
    gdf = gpd.read_file(input_file)
    print(f"Original CRS: {gdf.crs}")

    gdf_5070 = gdf.to_crs(epsg=5070)

    # gdf_5070.to_file(output_file)

    return gdf_5070


def read_data_as_gdf(file_path: str):
    """
    Read various file formats into a GeoDataFrame.
    Supported formats: .gdb, .geojson, .shp, .gpkg, .csv, .xlsx.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == ".gdb":
        layers = fiona.listlayers(file_path)
        if layers:
            return gpd.GeoDataFrame(
                gpd.read_file(file_path, layer=layers[0]), geometry="geometry"
            )
        else:
            raise ValueError("No layers found in the geodatabase.")

    elif file_extension == ".geojson":
        return gpd.read_file(file_path)

    elif file_extension == ".shp":
        return gpd.read_file(file_path)

    elif file_extension == ".gpkg":
        return gpd.read_file(file_path)

    elif file_extension == ".csv":
        df = pd.read_csv(file_path)
        # df['id'] = df.index
        if "LONGITUDE" in df and "LATITUDE" in df:
            return gpd.GeoDataFrame(
                df, geometry=gpd.points_from_xy(df.LONGITUDE, df.LATITUDE)
            )
        elif "Longitude" in df and "Latitude" in df:
            return gpd.GeoDataFrame(
                df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude)
            )
        elif "X" in df and "Y" in df:
            return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.X, df.Y))

    elif file_extension == ".xlsx":
        df = pd.read_excel(file_path)
        # df['id'] = df.index
        if "LONGITUDE" in df and "LATITUDE" in df:
            return gpd.GeoDataFrame(
                df, geometry=gpd.points_from_xy(df.LONGITUDE, df.LATITUDE)
            )
        elif "Longitude" in df and "Latitude" in df:
            return gpd.GeoDataFrame(
                df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude)
            )
        elif "X" in df and "Y" in df:
            return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.X, df.Y))

    else:
        raise ValueError(f"Unsupported file type: {file_extension}")
