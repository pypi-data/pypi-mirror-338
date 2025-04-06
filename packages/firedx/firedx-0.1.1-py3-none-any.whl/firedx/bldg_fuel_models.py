#!/usr/bin/env python3

"""
This script assigns building fuel models (1-13) to footprints based on relevant attributes.

Also provides command line usage to obtain building_fuel_models.csv file:
    ./bldg_fuel_models.py

To-do
- Replace with latest version
"""

import numpy as np
import pandas as pd
import geopandas as gpd

from firedx.footprints import calculate_bldg_metrics
from firedx.attributes import clean_height_stories


def _get_fuel_load_const(occtype_series: pd.Series) -> tuple:
    """Assign fuel loading constant and T_1MW based on occupancy type."""
    occ_fuel_load_const = {
        "RES": (700, "medium"),
        "COM": (650, "medium"),
        "IND": (750, "fast"),
    }  # MJ/m2 and t_1mw
    T_1MW_dict = {"slow": 600, "medium": 300, "fast": 150, "ultrafast": 75}  # seconds

    def _match_fuel_load(occtype):
        """Match an individual occupancy type."""
        for key in sorted(occ_fuel_load_const.keys(), key=len, reverse=True):
            if key in str(occtype):
                fuel_load, growth_rate = occ_fuel_load_const[key]
                return fuel_load, T_1MW_dict[growth_rate]
        return 700, T_1MW_dict["medium"]  # Default values: 700 MJ/m2, 300 seconds

    return occtype_series.apply(_match_fuel_load).apply(pd.Series)


def _get_fire_resistance(
    occtype: str, separation_distance: float, ch7A_compliance: bool
) -> str:
    """Determines the fire resistance level based on building attributes.

    Parameters:
        occupancy_type (str): A string containing 'RES', 'COM', or 'IND'
        separation_distance (float): Distance between structures in feet
        ch7A_compliance (bool): Whether the building is subject to CBC Ch. 7A/CRC R337 (Fire Hazard Severity Zone + Year Built > 2008)

    Returns:
        str: Fire resistance classification ("rated", "protected", or "unprotected")
    """
    occupancy_type = str(occtype).upper()

    if "RES" in occupancy_type:
        if separation_distance < 3:
            return "rated"
        return "protected" if ch7A_compliance else "unprotected"
    if separation_distance < 10:
        return "rated"
    return "protected" if ch7A_compliance else "unprotected"
    # elif accessory_utility and separation_distance < 50


def assign_bldgfm(buildings_gdf):
    buildings_gdf = buildings_gdf.reset_index(drop=True)

    ## ********************************
    ## BLDG AREA & NUMBER OF STORIES
    ## ********************************
    if (
        "BLDG_AREA_m2" not in buildings_gdf.columns
        or buildings_gdf["BLDG_AREA_m2"].isna().any()
        or (buildings_gdf["BLDG_AREA_m2"] == 0).any()
    ):
        missing_area_mask = buildings_gdf["BLDG_AREA_m2"].isna() | (
            buildings_gdf["BLDG_AREA_m2"] == 0
        )
        missing_bldgs = buildings_gdf[missing_area_mask]

        computed_metrics = calculate_bldg_metrics(missing_bldgs)
        buildings_gdf.loc[missing_area_mask, "BLDG_AREA_m2"] = computed_metrics[
            "BLDG_AREA_m2"
        ]

    if "num_story" not in buildings_gdf.columns:
        buildings_gdf = clean_height_stories(buildings_gdf)

    ## ********************************
    ## FIRE SIZE
    ## ********************************
    buildings_gdf[["FUEL_LOAD_DENSITY", "T_1MW"]] = _get_fuel_load_const(
        buildings_gdf["occtype"]
    )

    # Fire size calculation = (fuel load density)*(bldg area)*(number of stories + 1)
    # Additional "story" added to account for fuel loading of roof and walls
    buildings_gdf["FUEL_LOAD"] = (
        buildings_gdf["FUEL_LOAD_DENSITY"]
        * buildings_gdf["BLDG_AREA_m2"]
        * (buildings_gdf["num_story"] + 1)
    ).round(
        3
    ) / 1000  # GJ

    # Assign characteristic fire size (Rehm, 2008)
    buildings_gdf.loc[buildings_gdf["FUEL_LOAD"] < 360, "fire_size"] = "small"
    buildings_gdf.loc[
        (buildings_gdf["FUEL_LOAD"] >= 360) & (buildings_gdf["FUEL_LOAD"] < 720),
        "fire_size",
    ] = "moderate"
    buildings_gdf.loc[
        (buildings_gdf["FUEL_LOAD"] >= 720) & (buildings_gdf["FUEL_LOAD"] < 1440),
        "fire_size",
    ] = "large"
    buildings_gdf.loc[buildings_gdf["FUEL_LOAD"] >= 1440, "fire_size"] = "very large"

    ## ********************************
    ## FIRE RESISTANCE
    ## ********************************
    if "FHSZ" not in buildings_gdf.columns:
        buildings_gdf["FHSZ"] = np.nan

    year_built_col = next(
        (
            col
            for col in [
                "YR_BUILT",
                "YEAR_BUILT_JOINED",
                "YEAR_BUILT",
                "YEARBUILT",
                "med_yr_blt",
            ]
            if col in buildings_gdf.columns
        ),
        None,
    )

    if year_built_col:
        buildings_gdf["ch7A_compliance"] = (buildings_gdf[year_built_col] > 2008) & (
            buildings_gdf["FHSZ"].notna()
        )
    else:
        buildings_gdf["ch7A_compliance"] = False

    buildings_gdf["fire_resistance"] = buildings_gdf.apply(
        lambda row: _get_fire_resistance(
            row["occtype"], row["BLDG_SEPARATION_DIST_MIN"], row["ch7A_compliance"]
        ),
        axis=1,
    )

    ## ********************************
    ## ASSIGN BLDG_FUEL_MODEL
    ## ********************************

    # Mapping (fire_resistance, fire_size) -> BLDG_FUEL_MODEL
    fuel_model_map = {
        ("unprotected", "small"): 1,
        ("unprotected", "moderate"): 2,
        ("unprotected", "large"): 3,
        ("unprotected", "very large"): 4,
        ("protected", "small"): 5,
        ("protected", "moderate"): 6,
        ("protected", "large"): 7,
        ("protected", "very large"): 8,
        ("rated", "small"): 9,
        ("rated", "moderate"): 10,
        ("rated", "large"): 11,
        ("rated", "very large"): 12,
    }

    buildings_gdf["BLDG_FUEL_MODEL"] = buildings_gdf.apply(
        lambda row: fuel_model_map.get(
            (row["fire_resistance"], row["fire_size"]), "UNKNOWN"
        ),
        axis=1,
    )

    # Special case for buildings < 85 m²
    buildings_gdf.loc[buildings_gdf["BLDG_AREA_m2"] < 85, "BLDG_FUEL_MODEL"] = 13

    return buildings_gdf


def bldg_fuel_models():
    fuel_model_map = {
        ("unprotected", "small"): "ST01",
        ("unprotected", "moderate"): "ST02",
        ("unprotected", "large"): "ST03",
        ("unprotected", "very large"): "ST04",
        ("protected", "small"): "ST05",
        ("protected", "moderate"): "ST06",
        ("protected", "large"): "ST07",
        ("protected", "very large"): "ST08",
        ("rated", "small"): "ST09",
        ("rated", "moderate"): "ST10",
        ("rated", "large"): "ST11",
        ("rated", "very large"): "ST12",
        ("small_bldg", "any"): "ST13",  # Special case for buildings < 85 m²
    }

    fire_size_values = {
        "small": {"FUEL_LOAD": 360, "HRR_PEAK": 25, "T_EARLY": 100},
        "moderate": {"FUEL_LOAD": 720, "HRR_PEAK": 50, "T_EARLY": 150},
        "large": {"FUEL_LOAD": 1440, "HRR_PEAK": 100, "T_EARLY": 200},
        "very large": {"FUEL_LOAD": 7200, "HRR_PEAK": 500, "T_EARLY": 300},
    }

    fire_resistance_values = {
        "unprotected": {
            "FTP_CRIT": 10_500,
            "Q_CRIT": 9,
            "ABSORP": 0.89,
            "P_IGN": 100,
            "HARDENING_FACTOR": 0,
            "TAU_IGN": 20,
        },
        "protected": {
            "FTP_CRIT": 12_500,
            "Q_CRIT": 11,
            "ABSORP": 0.82,
            "P_IGN": 90,
            "HARDENING_FACTOR": 0.3,
            "TAU_IGN": 42,
        },
        "rated": {
            "FTP_CRIT": 15_500,
            "Q_CRIT": 13,
            "ABSORP": 0.79,
            "P_IGN": 70,
            "HARDENING_FACTOR": 0.7,
            "TAU_IGN": 60,
        },
    }

    # Constants
    NONBURNABLE_FRAC = 0.5  # not used, read from raster
    T_TOTAL_BURNING_TIME = 14400  # seconds (Rehm, 2008)
    T_1MW = 300  # seconds (medium growth rate for incipient stage)
    T_DECAY = 4320  # seconds (time at which 70% total fuel load is consumed)

    fuel_model_data = []

    for (fire_resistance, fire_size), model in fuel_model_map.items():
        if model == "ST13":
            height, t_early, t_fulldev, fuel_load, hrr_peak = 4, 75, 3600, 120, 21
            t_early_abs = T_1MW + t_early
            t_fulldev_abs = t_early_abs + t_fulldev
            t_decay_abs = T_DECAY + t_fulldev_abs
            ftp_crit, q_crit, absorptivity, p_ignition, hardening_factor, tau_ign = (
                10500,
                9,
                0.9,
                100,
                0,
                20,
            )
        else:
            height = (
                8 if fire_size in ["small", "moderate"] else 12
            )  # to be replaced with raster input for avg bldg height
            t_early = fire_size_values[fire_size]["T_EARLY"]
            t_fulldev = T_TOTAL_BURNING_TIME - (T_1MW + t_early + T_DECAY)
            t_early_abs = T_1MW + t_early
            t_fulldev_abs = t_early_abs + t_fulldev
            t_decay_abs = T_DECAY + t_fulldev_abs

            fuel_load = fire_size_values[fire_size]["FUEL_LOAD"]
            hrr_peak = fire_size_values[fire_size]["HRR_PEAK"]
            ftp_crit = fire_resistance_values[fire_resistance]["FTP_CRIT"]
            q_crit = fire_resistance_values[fire_resistance]["Q_CRIT"]
            absorptivity = fire_resistance_values[fire_resistance]["ABSORP"]
            p_ignition = fire_resistance_values[fire_resistance]["P_IGN"]
            hardening_factor = fire_resistance_values[fire_resistance][
                "HARDENING_FACTOR"
            ]
            tau_ign = fire_resistance_values[fire_resistance]["TAU_IGN"]

        fuel_model_numeric = int(model[2:])

        fuel_model_entry = {
            "FUEL_MODEL": fuel_model_numeric,
            "SHORTNAME": model,
            "T_1MW": T_1MW,  # seconds
            "T_EARLY": t_early_abs,  # seconds
            "T_FULLDEV": t_fulldev_abs,  # seconds
            "T_DECAY": t_decay_abs,  # seconds
            "FUEL_LOAD": fuel_load,  # GJ
            "HRR_PEAK": hrr_peak,  # MW
            "FTP_CRIT": ftp_crit,  # kJ/m²
            "Q_CRIT": q_crit,  # kW/m²
            "ABSORPTIVITY": absorptivity,  # [-]
            "HEIGHT": height,  # meters
            "NONBURNABLE_FRAC": NONBURNABLE_FRAC,  # [-]
            "P_IGNITION": p_ignition,  # [%]
            "HARDENING_FACTOR": hardening_factor,  # [-]
            "TAU_IGN": tau_ign,  # seconds
        }

        fuel_model_data.append(fuel_model_entry)

    fuel_model_table = pd.DataFrame(fuel_model_data)
    return fuel_model_table


if __name__ == "__main__":
    import os

    fuel_model_table = bldg_fuel_models()

    dir = "../data"

    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)

    csv_filename = os.path.join(dir, "building_fuel_models.csv")
    fuel_model_table.to_csv(csv_filename, index=False, header=False)
    print(f"Building fuel models table saved to {csv_filename}")
