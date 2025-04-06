# **FireDX**

A data engine for modeling and analyzing fire hazard and risk to communities and built assets. 

The FireDX library includes tools and functionality for extracting and transforming buildings and property data and generating datasets for use in wildland-urban fire spread modeling, fire exposure and risk analysis, and fire mitigation strategy evaluation.

Key features include: 

- **Urban Fuels Data Pipeline**
  - Generates vector and attribute datasets for urban fire risk analysis by extracting and standardizing buildings-related data from publicly available sources.
  - Preprocesses geospatial data to assign attributes that influence structure-level ignition susceptibility and burning characteristics for classification into Building Fuel Models.
  - Transforms data into structured, analysis-ready formats for downstream modeling and GIS tools.
  
- **Rasterization & Fire Model Inputs**
  - Produces raster inputs compatible with fire spread models that incorporate urban fire dynamics, such as WU-E (Wildland-Urban Extension) fire model implemented in [ELMFIRE](https://github.com/lautenberger/elmfire).
  - Supports automated rasterization of building footprints and fuels data, including conversion of the FBFM40.tif raster to differentiate buildings from nonburnable urban land cover (e.g., pavement).


Sample datasets generated using FireDX workflows are included in the `data/` directory.

---

## Installation

FireDX is implemented in Python and is best run in a controlled environment using Conda, particularly for management of geospatial package dependencies.

### **Prerequisites**

- Miniconda or Anaconda
- Git

---

### Option 1: Quick Start with Conda + pip (Recommended for Most Users)

This installs both system-level dependencies (e.g., GDAL, GEOS) and Python packages in a Conda environment, and then installs FireDX via pip.

1. **Clone the repo and update permissions**:
   ```bash
   git clone https://github.com/ma-th/firedx.git
   cd firedx
   chmod -R 755 ./*
   ```

2. **Create Conda environment with all dependencies**:
   ```bash
   conda env create -f environment.yaml
   conda activate firedx
   ```

3. **Install the `firedx` package into the environment**:
   ```bash
   pip install .
   ```

You can now import and use `firedx` in your scripts or notebooks.

---

### Option 2: Full Development Setup (Poetry + Conda)

If you want to **develop or contribute** to FireDX, it is recommended to install [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) using its official installer for dependency and dev tool management.


1. **Clone the repo and update permissions**:
   ```bash
   git clone https://github.com/ma-th/firedx.git
   cd firedx
   chmod -R 755 ./*
   ```

2. **Create Conda environment for system-level dependencies**:
   ```bash
   conda env create -f environment.yaml
   conda activate firedx
   ```

3. **Tell Poetry to use Conda's Python**:
   ```bash
   poetry config virtualenvs.create false --local
   ```

4. **Install project dependencies via Poetry**:
   ```bash
   poetry install
   ```

---

### Verifying Installation


```bash
conda activate firedx
python
>>> import firedx
>>> firedx.__version__
```

Or run tests (if using Poetry):

```bash
poetry run pytest
```

---

### Troubleshooting

- If you see errors related to `gdal`, `rasterio`, or `geopandas`, make sure you’re using the Conda environment created from `environment.yaml`.
- If `poetry install` creates a virtualenv, disable it with:
  ```bash
  poetry config virtualenvs.create false --local
  ```


---


## **Usage**

FireDX can be used to generate geospatial datasets and raster input decks for fire spread simulation and risk analysis. 

### Example 1: Generate Fire Model Input Rasters and Buildings Dataset

The current core functionality of FireDX is demonstrated in this example. The function below takes a FBFM40.tif raster as input, which should be a GeoTIFF file representing fuel models for a specific area of interest. For its corresponding area, the function generates an urban fuels (buildings) dataset in GeoJSON format and a raster input deck in GeoTIFF format for use with fire spread models. The new raster FBFM40b.tif replaces the original FBFM40.tif for fire modeling as it differentiates between burnable buildings and paved surfaces, which are both classified as the same "urban nonburnable" land cover (fuel model 91) in the original fuel model raster.

**Run**

Activate the Conda environment created from `environment.yaml`, navigate to the `examples/` directory, then run the following using either a Python interpreter or a terminal (tested on Linux/WSL2):

The optional `output_dir` argument specifies the directory where the generated files will be saved. If the directory does not exist, it will be created by the script.

- Python (Interpreter)

```python
from firedx import generate

# Generates an urban fuels dataset and a raster input deck for fire spread modeling
generate.main(fbfm40_path="./sample-data/fbfm40-sample.tif", output_dir="./sample-data/generated/")
```

- Command Line

```bash
python -m firedx.generate ./sample-data/fbfm40-sample.tif --output_dir=./sample-data/generated/
```

**Note:** You can run `python -m firedx.generate` from any location in your filesystem, as long as:
- The `firedx` package has been installed (e.g., via `pip install .`), and
- The Conda environment created from `environment.yaml` is activated.

---

### Additional Usage Guidance

See the [`examples/`](./examples/) directory for Jupyter notebooks that demonstrate different workflows using FireDX.

For detailed usage, refer to the [documentation](docs/USAGE.md).

---

## **Citation**

If you use the FireDX package in your work or derivative datasets, please cite as:


```bibtex
@misc{FireDX,
  author = {Maria F. Theodori},
  title = {FireDX: A Data Engine for Urban Fire Modeling and Risk Analysis},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ma-th/fireDX.git}}
}
```

Or, in APA Format:

Theodori, M. F. (2025). _FireDX: A data engine for urban fire modeling and risk analysis_ [Computer software]. GitHub. https://github.com/ma-th/fireDX.git

