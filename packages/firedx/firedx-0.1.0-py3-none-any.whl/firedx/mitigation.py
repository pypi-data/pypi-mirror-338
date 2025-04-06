import os
import rasterio
import geopandas as gpd
from rasterio.mask import mask
import numpy as np


def get_centerline():  # get centerline geometry of the fuel treatment polygons
    pass


def create_uniform_buffer():  # create a uniform buffer around the centerline
    # 150 ft buffer extending from each side of the centerline
    pass


def apply_fuel_treatments(raster_path, vector_path, output_fn="fbfm40-treatments.tif"):
    output_path = os.path.join(os.path.dirname(raster_path), output_fn)

    with rasterio.open(raster_path) as src:
        profile = src.profile
        raster_data = src.read(1)
        nodata_value = src.nodata
        raster_crs = src.crs

        vector_data = gpd.read_file(vector_path)
        vector_data = vector_data.to_crs(raster_crs)

        masked_raster, transform = mask(src, vector_data.geometry, crop=False)
        mask_indices = (masked_raster[0] != nodata_value) & (masked_raster[0] != 0)

        modified_raster = raster_data.copy()

        # Apply the conditions for fuel treatments within the polygons mask
        modified_raster[mask_indices & (raster_data == 122)] = 121  # GS2 to GS1
        modified_raster[mask_indices & (raster_data == 145)] = 144  # SH5 to SH4
        modified_raster[mask_indices & (raster_data == 165)] = 161  # TU5 to TU1
        modified_raster[mask_indices & (raster_data == 185)] = 183  # TL5 to TL3
        modified_raster[mask_indices & (raster_data == 189)] = 182  # TL9 to TL2

    with rasterio.open(output_path, "w", **profile) as dst:
        dst.write(modified_raster, 1)

    print(f"Modified raster saved to {output_path}")


# Example usage
# apply_fuel_treatments("fbfm40.tif", "treatments_polygons.shp")
apply_fuel_treatments(
    "../projects/jfsp/2024-11-03_INPUTS/fbfm40.tif",
    "../projects/jfsp/2024-11-03_INPUTS/KonoctiInterface_Units/KI_Units.shp",
)
