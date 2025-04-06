#!/usr/bin/env python3

import os
import glob

import numpy as np
import geopandas as gpd
import rasterio
from rasterio.enums import Resampling
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio import windows

import shapely.geometry
from shapely.geometry import box


def get_raster_info(raster_path):
    with rasterio.open(raster_path) as src:
        return os.path.basename(raster_path), src.crs


def check_raster_consistency(directory):
    raster_files = glob.glob(os.path.join(directory, "*.tif"))
    if not raster_files:
        print("No raster files found in the directory.")
        return

    raster_name, first_raster_crs = get_raster_info(raster_files[0])
    print("first raster check: ", raster_name, "\n\n", first_raster_crs)

    for raster_file in raster_files[1:]:
        raster_name, crs = get_raster_info(raster_file)

        if crs != first_raster_crs:
            print(f"Raster '{raster_file}' does not match: CRS {crs}")


def raster_cells_to_polygons(
    raster_data, raster_crs, raster_res, raster_bounds, target_value="all"
):
    # with rasterio.open(raster_file) as src:
    #    raster_data = src.read(1)
    #    raster_crs = src.crs
    #    cell_width, cell_height = src.res
    #    raster_bounds = src.bounds

    if target_value == 91:
        rows, cols = np.where(raster_data[0] == target_value)
    elif target_value == "all":
        rows, cols = np.indices(raster_data[0].shape)
        rows, cols = rows.flatten(), cols.flatten()
    else:
        raise ValueError("Invalid target_value. Use 91 or 'all'.")

    cell_width, cell_height = raster_res[0], raster_res[1]

    grid_cells = [
        box(
            raster_bounds.left + col * cell_width,
            raster_bounds.bottom + row * cell_height,
            raster_bounds.left + (col + 1) * cell_width,
            raster_bounds.bottom + (row + 1) * cell_height,
        )
        for row, col in zip(rows, cols)
    ]

    gdf = gpd.GeoDataFrame(geometry=grid_cells, crs=raster_crs)
    return gdf


def modify_fm(fbfm40_data, fbfm40_profile, working_dir):
    os.chdir(working_dir)

    bfm_path = "bfm13.tif"

    with rasterio.open(bfm_path) as bfm_src:
        bfm_data = bfm_src.read()
        bfm_profile = bfm_src.profile

    if fbfm40_profile != bfm_profile:
        raise ValueError("Raster profiles do not match!")

    # Modify FBFM cells to distinguish buildings vs roadways
    fbfm40_data[fbfm40_data == 91] = 256
    fbfm40_data[(bfm_data > 0)] = 91

    fbfm40b_fn = "fbfm40b.tif"
    with rasterio.open(fbfm40b_fn, "w", **fbfm40_profile) as dst:
        dst.write(fbfm40_data)
        dst.close()

    print("Modified FBFM40 input raster saved as:", fbfm40b_fn)

    # Update BFM cells that are non-buildings
    veg_mask = (fbfm40_data > 99) & (fbfm40_data < 256)
    agriculture_mask = fbfm40_data == 93
    road_mask = fbfm40_data == 91
    water_mask = fbfm40_data == 98
    other_nonburnable_mask = (fbfm40_data == 92) | (fbfm40_data == 99)

    bfm_data[(bfm_data == -9999) & veg_mask] = 0
    bfm_data[(bfm_data == -9999) & agriculture_mask] = (
        93  # to set agriculture in the bfm13 raster, can set burnable parameters if needed
    )
    bfm_data[(bfm_data == -9999) & road_mask] = (
        91  # to set roadways in the bfm13 raster
    )
    bfm_data[(bfm_data == -9999) & water_mask] = 98  # to set water in the bfm13 raster
    bfm_data[(bfm_data == -9999) & other_nonburnable_mask] = (
        99  # to set snow/ice/barren in the bfm13 raster
    )

    with rasterio.open(bfm_path, "w", **bfm_profile) as dst:
        dst.write(bfm_data)
        dst.close()

    print("Updated BFM13 input raster saved as:", bfm_path)


def mask_fuel_areas(input_raster_path):
    output_raster_path = os.path.join(
        os.path.basename(input_raster_path), "fbfm40b-limited.tif"
    )
    with rasterio.open(input_raster_path) as src:
        data = src.read()
        bottom_third_start = (
            data.shape[1] * 2 // 3
        )  # Assuming data.shape = (bands, rows, cols)

        data[:, bottom_third_start:, :] = 99

        out_meta = src.meta.copy()

        with rasterio.open(output_raster_path, "w", **out_meta) as dst:
            dst.write(data)

    print(f"Modified raster saved to: {output_raster_path}")


def set_nodata_and_save(input_raster_path, output_raster_path, new_nodata_value):

    with rasterio.open(input_raster_path) as src:

        data = src.read()

        profile = src.profile
        profile.update(nodata=new_nodata_value)

        if src.nodata is not None:
            data[data == src.nodata] = new_nodata_value

        with rasterio.open(output_raster_path, "w", **profile) as dst:
            dst.write(data)

    print(
        f"The no-data value has been set to {new_nodata_value} and saved to: {output_raster_path}"
    )


def crop_raster_to_reference(
    input_raster_path, reference_raster_path, output_cropped_path
):
    """
    Crops the input raster to match the extent of the reference raster.
    Saves the cropped raster to the specified output path.
    """
    with rasterio.open(reference_raster_path) as ref_src:
        ref_bounds = ref_src.bounds

    with rasterio.open(input_raster_path) as src:
        window = windows.from_bounds(*ref_bounds, transform=src.transform)
        transform = src.window_transform(window)
        data = src.read(window=window)
        profile = src.profile

        profile.update(
            {
                "height": data.shape[1],
                "width": data.shape[2],
                "transform": transform,
                "crs": src.crs,
            }
        )

        with rasterio.open(output_cropped_path, "w", **profile) as dst:
            dst.write(data)

    print(f"Cropped raster saved to: {output_cropped_path}")
    return output_cropped_path


def resample_raster(input_raster_path, output_resampled_path, new_resolution=10):
    """
    Resamples the input raster to the specified resolution.
    Saves the resampled raster to the specified output path.
    """
    with rasterio.open(input_raster_path) as src:
        # Calculate new dimensions for the new resolution
        scale_factor = src.res[0] / new_resolution
        new_width = int(src.width * scale_factor)
        new_height = int(src.height * scale_factor)

        transform, width, height = calculate_default_transform(
            src.crs, src.crs, new_width, new_height, *src.bounds
        )

        profile = src.profile.copy()
        profile.update(
            {"height": new_height, "width": new_width, "transform": transform}
        )

        resampled_data = np.zeros(
            (src.count, new_height, new_width), dtype=profile["dtype"]
        )

        # Resample the raster
        with rasterio.open(output_resampled_path, "w", **profile) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=resampled_data[i - 1],
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=src.crs,
                    resampling=Resampling.nearest,
                )
                dst.write(resampled_data[i - 1], indexes=i)

    print(f"Resampled raster saved to: {output_resampled_path}")
    return output_resampled_path


def crop_resample(input_raster_path, reference_raster_path, output_cropped_path):
    """
    Crops and resamples the input raster to match the extent, CRS, transform, and block size of the reference raster.
    The output raster retains the datatype and actual data (resampled) of the input raster.
    Saves the cropped raster to the specified output path.
    """
    with rasterio.open(reference_raster_path) as ref_src:
        ref_profile = ref_src.profile.copy()
        ref_transform = ref_src.transform
        ref_crs = ref_src.crs
        ref_height = ref_src.height
        ref_width = ref_src.width

    with rasterio.open(input_raster_path) as src:
        # Update reference profile with input's datatype and band count
        ref_profile.update({"dtype": src.dtypes[0], "count": src.count})

        # Initialize destination array with input's nodata value if available
        input_nodata = src.nodata
        if input_nodata is not None:
            data = np.full(
                (src.count, ref_height, ref_width),
                input_nodata,
                dtype=ref_profile["dtype"],
            )
        else:
            data = np.zeros(
                (src.count, ref_height, ref_width), dtype=ref_profile["dtype"]
            )

        reproject(
            source=rasterio.band(src, list(range(1, src.count + 1))),
            destination=data,
            src_transform=src.transform,
            src_crs=src.crs,
            dst_transform=ref_transform,
            dst_crs=ref_crs,
            resampling=Resampling.nearest,
            src_nodata=input_nodata,
            dst_nodata=input_nodata,
        )

        with rasterio.open(output_cropped_path, "w", **ref_profile) as dst:
            dst.write(data)

    print(f"Cropped raster saved to: {output_cropped_path}")
    return output_cropped_path


def batch_crop_rasters(input_dir, reference_raster_path, output_dir):
    """Process all TIFF files in a directory to match a reference raster's profile."""
    os.makedirs(output_dir, exist_ok=True)

    tif_files = glob.glob(os.path.join(input_dir, "*.tif"))

    for input_tif in tif_files:
        fname = os.path.basename(input_tif)
        output_path = os.path.join(output_dir, f"cropped_{fname}")

        print(f"Processing: {fname}")
        try:
            crop_raster_to_reference(
                input_raster_path=input_tif,
                reference_raster_path=reference_raster_path,
                output_cropped_path=output_path,
            )
        except Exception as e:
            print(f"Failed to process {fname}: {str(e)}")

    print(f"Processed {len(tif_files)} files. Outputs saved to: {output_dir}")
