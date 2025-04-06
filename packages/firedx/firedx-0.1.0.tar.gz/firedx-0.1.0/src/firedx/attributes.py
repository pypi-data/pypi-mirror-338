import os
import json
import shutil
import zipfile
from collections import Counter

import requests
from tqdm import tqdm
import numpy as np
import pandas as pd
import geopandas as gpd
import shapely.geometry
import pickle


def _most_common_or_first(series):
    """
    Custom aggregation function to return the most common value in a series.
    If there's a tie, it returns the first value.
    """
    if series.empty:
        return None
    counts = Counter(series)
    most_common = counts.most_common()
    if len(most_common) == 1 or most_common[0][1] != most_common[1][1]:
        return most_common[0][0]  # Return the most common value
    return series.iloc[0]  # Return the first value if there's a tie


def clean_year_built(df):
    """
    YEAR_BUILT is typically from parcel data
    YEARBUILT or YR_BUILT is typically from DINS data
    med_yr_blt is from NSI data
    """
    df["YEAR_BUILT_JOINED"] = np.nan

    if "YEAR_BUILT" in df.columns:
        df["YEAR_BUILT_JOINED"] = df["YEAR_BUILT"].replace(0, np.nan).round()
    elif "YEARBUILT" in df.columns:
        df["YEAR_BUILT_JOINED"] = df["YEARBUILT"].replace(0, np.nan).round()
    elif "YR_BUILT" in df.columns:
        df["YEAR_BUILT_JOINED"] = df["YR_BUILT"].replace(0, np.nan).round()
    elif "med_yr_blt" in df.columns:
        df["YEAR_BUILT_JOINED"] = df["med_yr_blt"].replace(0, np.nan).round()

    df["YEAR_BUILT_JOINED"] = pd.to_numeric(df["YEAR_BUILT_JOINED"], errors="coerce")

    year_built_col = "med_yr_blt"  # fallback value

    if year_built_col:
        # Replace NaN or years < 1800 with values from year_built_col, only if year_built_col is not NaN
        df["YEAR_BUILT_JOINED"] = np.where(
            (df["YEAR_BUILT_JOINED"].isna() | (df["YEAR_BUILT_JOINED"] < 1800))
            & df[year_built_col].notna(),
            df[year_built_col],
            df["YEAR_BUILT_JOINED"],
        )

        df["YEAR_BUILT_JOINED"] = pd.to_numeric(
            df["YEAR_BUILT_JOINED"], errors="coerce"
        )

    return df


def clean_height_stories(df):
    if "height" in df.columns:
        df["BLDG_HEIGHT"] = (
            df["height"].fillna((df["num_story"] * 3) + 1).round(3).fillna(4)
        )
        df.drop(columns="height", inplace=True)
    else:
        df["BLDG_HEIGHT"] = ((df["num_story"] * 3) + 1).round(3).fillna(4)

    if "num_story" in df.columns:
        df["num_story"] = (
            df["num_story"].fillna(((df["BLDG_HEIGHT"] - 1) / 3).round()).astype(int)
        )
    else:
        df["num_story"] = ((df["BLDG_HEIGHT"] - 1) / 3).round().fillna(1).astype(int)

    return df


def get_intersecting_counties(aoi_geojson):
    """
    Find all counties that intersect with a given polygon GeoJSON.

    Parameters:
        aoi_geojson (dict): AOI geometry in GeoJSON-like dictionary.

    Returns:
        A dictionary of names and fips codes of counties that intersect with the AOI.
    """
    counties_response = requests.get(
        "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
    )
    counties_geojson = counties_response.json()
    counties_gdf = gpd.GeoDataFrame.from_features(counties_geojson["features"])
    counties_gdf = counties_gdf.set_crs("EPSG:4326")

    intersecting_counties = counties_gdf[
        counties_gdf.geometry.intersects(
            shapely.geometry.shape(aoi_geojson.get("geometry"))
        )
    ]
    counties_dict = dict(
        zip(
            intersecting_counties["NAME"],
            (intersecting_counties["STATE"] + intersecting_counties["COUNTY"]),
        )
    )

    return counties_dict


def get_parcel_data(
    aoi_geojson, zip_path="../data/NPDP_Parcel_data.zip", target_crs="EPSG:4326"
):
    """
    Extracts parcel data for the counties in 'counties_list' from a nested .zip file structure.

    Parameters:
        aoi_geojson (dict): AOI geometry in GeoJSON-like dictionary.
        zip_path (str): Path to the .zip file containing parcel data.

    Returns:
        GeoDataFrame: Concatenated parcel data for the specified counties.
    """
    counties_dict = get_intersecting_counties(aoi_geojson)
    # print(f"Counties to process: {list(counties_dict)}")

    bad_parcels = ["Butte", "Yuba", "Mendocino"]

    for key in bad_parcels:
        if counties_dict.get(key):
            print(f"{key} County parcel data not available.")
        counties_dict.pop(key, None)

    parcels_gdfs = []

    # zip_path = os.path.expanduser(zip_path)
    with zipfile.ZipFile(zip_path, "r") as top_zip:
        top_level_files = top_zip.namelist()

        county_zip_files = [
            f
            for f in top_level_files
            if any(fips in f for fips in list(counties_dict.values()))
            and f.endswith(".ZIP")
        ]
        print(
            f"Filtered county ZIP files: {county_zip_files}"
        )  # Debug: print filtered files

        for county_zip_file in county_zip_files:
            # print(f"Processing county ZIP: {county_zip_file}")  # Debug: print current file
            extracted_dir = (
                "./temp_extracted"  # Extract the sub-zip file to a temporary directory
            )
            os.makedirs(extracted_dir, exist_ok=True)

            with top_zip.open(county_zip_file) as county_zip:
                county_zip_path = os.path.join(
                    extracted_dir, os.path.basename(county_zip_file)
                )

                with open(county_zip_path, "wb") as f:
                    f.write(county_zip.read())

                with zipfile.ZipFile(county_zip_path, "r") as county_zip_ref:
                    county_files = county_zip_ref.namelist()

                    parcels_shapefile = next(
                        (f for f in county_files if f.endswith("/parcels.shp")), None
                    )

                    if parcels_shapefile:
                        # print(f"Found parcels.shp: {parcels_shapefile}")  # Debug: print found shapefile
                        for file in county_files:
                            if file.startswith(os.path.dirname(parcels_shapefile)):
                                county_zip_ref.extract(file, path=extracted_dir)

                        shapefile_path = os.path.join(extracted_dir, parcels_shapefile)
                        try:
                            parcels_gdf = gpd.read_file(shapefile_path)

                            if parcels_gdf.crs != target_crs:
                                parcels_gdf = parcels_gdf.to_crs(target_crs)

                            parcels_gdfs.append(parcels_gdf)
                        except Exception as e:
                            print(f"Error reading shapefile {shapefile_path}: {e}")

    if parcels_gdfs:
        all_parcels_gdf = gpd.GeoDataFrame(
            pd.concat(parcels_gdfs, ignore_index=True), crs=target_crs
        )
    else:
        all_parcels_gdf = gpd.GeoDataFrame()  # Empty if no data found

    shutil.rmtree("./temp_extracted", ignore_errors=True)

    aoi_parcels_gdf = all_parcels_gdf[
        all_parcels_gdf.intersects(
            shapely.geometry.shape(aoi_geojson.get("geometry")).buffer(0.02)
        )
    ]

    return aoi_parcels_gdf


def join_parcel_data(bldgs_gdf, parcels_gdf):
    """Joins building data with parcel data based on spatial intersection.

    Args:
        bldgs_gdf (GeoDataFrame): Building footprints geometry
        parcels_gdf (GeoDataFrame): Parcel data geometry with attributes

    Returns:
        GeoDataFrame: Merged GeoDataFrame with footprints geometry and added parcel attributes
    """
    if bldgs_gdf.crs != parcels_gdf.crs:
        parcels_gdf = parcels_gdf.to_crs(bldgs_gdf.crs)

    parcels_gdf["parcel_id"] = parcels_gdf.index

    geom_type = bldgs_gdf.geom_type.unique()

    if "Point" in geom_type or "MultiPoint" in geom_type:
        # If bldgs are points, perform a direct spatial join
        merged_gdf = gpd.sjoin(
            bldgs_gdf, parcels_gdf, how="left", predicate="intersects"
        )

        # merged_gdf.rename(columns={'index_right': 'max_parcel_id'}, inplace=True)
        # merged_gdf['max_parcel_id'] = merged_gdf['max_parcel_id'].apply(lambda x: int(x) if pd.notnull(x) else x)

    else:
        parcel_sindex = parcels_gdf.sindex
        max_overlap_ids = []

        for i, bldg in bldgs_gdf.iterrows():
            possible_matches_index = list(
                parcel_sindex.intersection(bldg.geometry.bounds)
            )
            possible_matches = parcels_gdf.iloc[possible_matches_index]

            overlaps = possible_matches.geometry.apply(
                lambda parcel: bldg.geometry.intersection(parcel).area
            )

            if overlaps.empty or overlaps.max() == 0:
                max_overlap_id = None
            else:
                max_overlap_id = overlaps.idxmax()

            max_overlap_ids.append(max_overlap_id)

        bldgs_gdf["max_parcel_id"] = max_overlap_ids
        bldgs_gdf["max_parcel_id"] = bldgs_gdf["max_parcel_id"].apply(
            lambda x: int(x) if pd.notnull(x) else x
        )

        # If bldgs are polygons, perform the 1-to-1 merge based on greatest overlap
        merged_gdf = bldgs_gdf.merge(
            parcels_gdf,
            left_on="max_parcel_id",
            right_on="parcel_id",
            how="left",
            suffixes=("", "_parcel"),
        )

    merged_gdf = merged_gdf.drop(
        columns=["geometry_parcel"], errors="ignore"
    ).set_geometry("geometry")
    merged_gdf.drop(
        columns=[
            "Id",
            "BLDG_AREA_parcel",
            "DEED_DSCR",
            "ASSMT_YEAR",
            "REC_DATE",
            "XCOORD",
            "YCOORD",
            "MINX",
            "MINY",
            "MAXX",
            "MAXY",
            "ATTDATE",
            "VERSION",
            "QUANTARIUM",
        ],
        inplace=True,
    )

    return merged_gdf


def get_nsi_data(aoi_geojson):
    response = requests.post(
        url="https://nsi.sec.usace.army.mil/nsiapi/structures?fmt=fc",
        json=aoi_geojson,
    )

    if response.status_code == 200:
        nsi_gdf = gpd.GeoDataFrame.from_features(
            response.json()["features"], crs="EPSG:4326"
        )
        # nsi_gdf.to_file(f'{output_dir}' + '/nsi_raw.geojson', driver='GeoJSON')
        return nsi_gdf
    else:
        print(f"Failed to get data from NSI API. Status code: {response.status_code}")
        # sys.exit(f"Script terminated due to unsuccessful data retrieval. Status code: {response.status_code}")


def join_nsi_data(polygons_gdf, nsi_gdf, buffer_distance=200):
    """
    Joins NSI point data to polygon data with custom aggregation for 1-to-1 matching.

    Parameters:
        polygons_gdf (GeoDataFrame): Building footprints or polygons.
        nsi_gdf (GeoDataFrame): NSI attributes.
        buffer_distance (float): Buffer distance for proximity join.

    Returns:
        GeoDataFrame: GeoDataFrame with NSI attributes joined to polygons.
    """

    def _aggregate_attributes(gdf, on="geometry"):
        return gdf.groupby(on).agg(
            {
                "occtype": _most_common_or_first,  #'st_damcat': _most_common_or_first,
                "bldgtype": _most_common_or_first,
                "found_type": _most_common_or_first,
                "num_story": "mean",
                "found_ht": "mean",
                "val_struct": "mean",
                "val_cont": "mean",
                "val_vehic": "mean",
                "med_yr_blt": "mean",
                #'ground_elv': 'mean', 'ground_elv_m': 'mean'
            }
        )

    if polygons_gdf.crs != nsi_gdf.crs:
        nsi_gdf = nsi_gdf.to_crs(polygons_gdf.crs)

    crs_is_degrees = polygons_gdf.crs.to_string().lower().find("degree") != -1

    if crs_is_degrees:
        buffer_distance = 200 / 111_320  # ~1 degree = 111.32 km at the equator

    # Initial spatial join and aggregation
    joined_gdf = gpd.sjoin(polygons_gdf, nsi_gdf, how="left", predicate="intersects")
    aggregated_gdf = polygons_gdf.merge(
        _aggregate_attributes(joined_gdf), on="geometry"
    )

    # Proximity join for unmatched polygons
    unmatched_polys = aggregated_gdf[aggregated_gdf["occtype"].isna()].copy()
    unmatched_polys["geometry"] = unmatched_polys.geometry.buffer(buffer_distance)

    proximity_joined = gpd.sjoin(
        unmatched_polys[["geometry"]], nsi_gdf, how="left", predicate="intersects"
    )
    proximity_aggregated = _aggregate_attributes(
        proximity_joined, on=proximity_joined.index
    )

    # Update unmatched rows with proximity-aggregated values
    columns_to_update = list(proximity_aggregated.columns)
    aligned_indices = aggregated_gdf.index.intersection(proximity_aggregated.index)

    aggregated_gdf.loc[aligned_indices, columns_to_update] = proximity_aggregated.loc[
        aligned_indices, columns_to_update
    ]

    return aggregated_gdf


def get_feature_layers(url, aoi_geojson, where="1=1", batch_size=2000, return_all=True):
    """
    Fetches ALL data from REST Feature Servers (handles pagination) and returns a GeoDataFrame.

    Parameters:
        url (str): Base URL of the FeatureServer layer (ending in /FeatureServer/x).
        aoi_geojson (dict): AOI geometry in GeoJSON-like dictionary for spatial query (use EPSG:4326).
        where (str): SQL WHERE clause to filter results (default is "1=1" for all features).
        batch_size (int): Number of records per request (default is 2000, the API max limit).
        return_all (bool): Whether to retrieve all features or just a batch.

    Returns:
        GeoDataFrame: A GeoPandas DataFrame containing all available features.
    """
    if not (aoi_geojson and aoi_geojson.get("type") == "Polygon"):
        raise Warning(
            "No features fetched from service URL. Only Polygon geometries are supported for spatial query."
        )

    aoi_geometry = {
        "rings": aoi_geojson["coordinates"],
        "spatialReference": {"wkid": 4326},
    }

    def _get_request_params(offset=0, count_only=False):
        """Helper function to construct request parameters."""
        return {
            "where": where,
            "geometry": json.dumps(aoi_geometry),
            "geometryType": "esriGeometryPolygon",
            "inSR": "4326",
            "spatialRel": "esriSpatialRelIntersects",
            "distance": 30,
            "units": "esriSRUnit_Meter",
            "f": "json" if count_only else "geojson",
            "returnCountOnly": "true" if count_only else "false",
            "resultOffset": offset if not count_only else None,
            "resultRecordCount": batch_size if not count_only else None,
            "outFields": "*" if not count_only else None,
        }

    def _convert_date_columns(gdf):
        """Helper function to convert date columns to datetime format."""
        date_cols = [
            col
            for col in gdf.columns
            if any(keyword in col.lower() for keyword in ["date"])
        ]
        for col in date_cols:
            gdf[col] = (
                pd.to_datetime(gdf[col], unit="ms", errors="coerce")
                if pd.api.types.is_numeric_dtype(gdf[col])
                else pd.to_datetime(gdf[col], errors="coerce")
            )
        return gdf

    # Fetch total count intersecting AOI geometry
    response = requests.get(f"{url}/query", params=_get_request_params(count_only=True))
    if response.status_code != 200:
        raise ValueError(
            f"Error fetching feature count: {response.status_code} - {response.text}"
        )

    total_features = response.json().get("count", 0)
    if total_features == 0:
        raise ValueError("No features found for the given query.")

    print(
        f"Retrieving {'all' if return_all else batch_size} of {total_features} intersecting features from REST APIs."
    )

    all_gdfs = []
    offset = 0

    with tqdm(total=total_features if return_all else batch_size, disable=True) as pbar:
        while True:
            response = requests.get(
                f"{url}/query", params=_get_request_params(offset=offset)
            )

            if response.status_code != 200:
                raise ValueError(
                    f"Error fetching data: {response.status_code} - {response.text}"
                )

            try:
                gdf = gpd.read_file(response.text)
                if gdf.empty:
                    break

                gdf = _convert_date_columns(gdf)  # Convert date columns
                all_gdfs.append(gdf)
                offset += batch_size
                pbar.update(len(gdf))

                if not return_all and sum(len(df) for df in all_gdfs) >= batch_size:
                    break

            except Exception as e:
                raise ValueError(f"Failed to parse GeoDataFrame: {e}")

    if all_gdfs:
        return pd.concat(all_gdfs, ignore_index=True)

    raise ValueError("No data retrieved from the server.")


def join_feature_layers(footprints_gdf, feature_layers):
    """
    Joins attributes from queried features with the footprints GeoDataFrame.

    Parameters:
        footprints_gdf (GeoDataFrame): GeoDataFrame of building footprints.
        feature_layers (list): List of GeoDataFrames queried from REST services.

    Returns:
        GeoDataFrame: A GeoDataFrame with joined data from all feature services queried.
    """
    if not feature_layers:
        return footprints_gdf

    joined_gdf = footprints_gdf.copy()

    for feature_gdf in feature_layers:
        if feature_gdf.empty:
            continue

        if feature_gdf.crs != joined_gdf.crs:
            feature_gdf = feature_gdf.to_crs(joined_gdf.crs)

        joined_gdf = gpd.sjoin(
            joined_gdf, feature_gdf, how="left", predicate="intersects"
        )
        joined_gdf.drop(columns=["index_right"], inplace=True, errors="ignore")

    return joined_gdf


def join_feature_layers_pts(footprints_gdf, feature_layers):
    """
    Joins attributes from queried features with the footprints GeoDataFrame based on a centroid (representative point) intersection.

    Parameters:
        footprints_gdf (GeoDataFrame): GeoDataFrame of building footprints.
        feature_layers (list): List of GeoDataFrames queried from REST services or other sources.

    Returns:
        GeoDataFrame: A GeoDataFrame with attributes joined from all feature layers.
    """

    if not feature_layers:
        return footprints_gdf

    points_gdf = footprints_gdf.copy()
    points_gdf["geometry"] = footprints_gdf.geometry.representative_point()
    points_gdf["original_index"] = points_gdf.index

    attributes_dfs = []

    for feature_gdf in feature_layers:
        if feature_gdf.empty:
            continue

        if feature_gdf.crs != points_gdf.crs:
            feature_gdf = feature_gdf.to_crs(points_gdf.crs)

        # Spatial join using representative points of the footprints polygons
        joined_pts = gpd.sjoin(points_gdf, feature_gdf, how="left", predicate="within")
        # joined_pts = gpd.sjoin_nearest(points_gdf, feature_gdf, how="left", max_distance=8,distance_col="sjoin_dist")
        joined_pts.drop(columns=["index_right"], inplace=True, errors="ignore")

        feature_columns = [
            col
            for col in joined_pts.columns
            if col not in ["geometry", "original_index"]
        ]

        if feature_columns:
            tmp_df = joined_pts.set_index("original_index")[feature_columns]
            attributes_dfs.append(tmp_df)

    if not attributes_dfs:
        return footprints_gdf

    merged_attributes_df = pd.concat(attributes_dfs, axis=1)

    duplicate_columns = set(merged_attributes_df.columns).intersection(
        footprints_gdf.columns
    )
    merged_attributes_df.drop(columns=duplicate_columns, inplace=True, errors="ignore")

    joined_gdf = footprints_gdf.merge(
        merged_attributes_df, left_index=True, right_index=True, how="left"
    )
    joined_gdf = gpd.GeoDataFrame(
        joined_gdf, geometry="geometry", crs=footprints_gdf.crs
    )

    return joined_gdf


def pickle_query(pickle_file_path, aoi_geojson, target_crs=None):
    """
    Query features from a pickle file that intersect the AOI defined by a GeoJSON dictionary.
    Uses a local projected CRS (UTM) for better performance and accuracy.

    Parameters:
        pickle_file_path (str): Path to the input pickle file.
        aoi_geojson (dict): AOI geometry in GeoJSON-like dictionary (EPSG:4326).
        target_crs (str, optional): Projected CRS for spatial operations (default: UTM zone based on AOI).

    Returns:
        GeoDataFrame: GeoDataFrame of features that intersect the AOI.
    """
    try:
        with open(pickle_file_path, "rb") as f:
            gdf = pickle.load(f)

        if gdf.crs is None:
            raise ValueError("GeoDataFrame does not have a CRS. Please assign one.")

        aoi_geom = shapely.geometry.shape(aoi_geojson["geometry"])
        aoi_gdf = gpd.GeoDataFrame(geometry=[aoi_geom], crs="EPSG:4326")

        if target_crs is None:
            lon, lat = aoi_geom.centroid.x, aoi_geom.centroid.y
            utm_zone = int((lon + 180) / 6) + 1
            target_crs = f"EPSG:{32600 + utm_zone if lat >= 0 else 32700 + utm_zone}"

        gdf = gdf.to_crs(target_crs)
        aoi_gdf = aoi_gdf.to_crs(target_crs)

        filtered_gdf = gdf[gdf.intersects(aoi_gdf.geometry.iloc[0])]

        return filtered_gdf

    except Exception as e:
        print(f"Error: {e}")
        return None


def join_to_footprints(
    footprints_gdf,
    aoi_geojson,
    aoi_crs,
    parcel_data_path="../data/NPDP_Parcel_data.zip",
):
    """
    Joins various data sources as attributes to the footprints GeoDataFrame.

    Parameters:
        footprints_gdf (GeoDataFrame): GeoDataFrame of building footprints.
        aoi_geojson (dict): AOI geometry in GeoJSON-like dictionary (EPSG:4326).
        aoi_crs (str): CRS of the AOI.

    Returns:
        GeoDataFrame: A GeoDataFrame with all joined data sources, reprojected to `aoi_crs`.
    """
    nsi_gdf = get_nsi_data(aoi_geojson)
    footprints_nsi_joined = join_nsi_data(footprints_gdf, nsi_gdf)

    if os.path.exists(parcel_data_path):
        parcels_gdf = get_parcel_data(aoi_geojson)
        footprints_parcels_joined = join_parcel_data(footprints_nsi_joined, parcels_gdf)
    else:
        # print("Parcel data not found. Skipping parcel data join...")
        footprints_parcels_joined = footprints_nsi_joined  # Skip parcel data

    footprints_cleaned = clean_year_built(footprints_parcels_joined)
    footprints_cleaned = clean_height_stories(footprints_cleaned)

    feature_services = {
        "fhsz": "https://services1.arcgis.com/jUJYIo9tSA7EHvfZ/arcgis/rest/services/FHSZ_SRA_LRA_Combined/FeatureServer/0",
        # additional urls can be handled
    }

    feature_layers = []
    for key, url in feature_services.items():
        feature_data = get_feature_layers(url, aoi_geojson.get("geometry"))
        if feature_data.empty:
            print(f"No {key} features data found")
        else:
            feature_layers.append(feature_data)

    # buildings_gdf = join_feature_layers(footprints_cleaned, feature_layers)
    buildings_gdf = join_feature_layers_pts(footprints_cleaned, feature_layers)

    buildings_gdf.drop(
        columns=[
            "OBJECTID",
            "Shape__Area",
            "Shape__Length",
            "FHSZ_Description",
            "SRA_Previous",
            "SRA22_2",
            "FHSZ_7Class",
        ],
        inplace=True,
    )

    if buildings_gdf.crs != aoi_crs:
        buildings_gdf = buildings_gdf.to_crs(aoi_crs)

    print("Spatial join of attributes completed.")

    return buildings_gdf
