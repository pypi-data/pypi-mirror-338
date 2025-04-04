# Qimchi

Plotly based data visualization tool for xarray data. Optimized to work with the [qcutils](https://gitlab.com/squad-lab/qcutils) package. Qimchi expects the data to be `zarr` formatted xarray files, documentation for handling these files can be found [here](https://xarray.pydata.org/en/stable/io.html#zarr).

## Installation 

### With uv
> ☀️ **RECOMMENDED** ☀️

#### Install `uv`
Follow the official instructions from [Astral's website](https://astral.sh/uv/). `uv` manages virtual environments and dependencies for you, making it easier to work with Python packages. For this project, we include the lock file which allows you to use the exact package versions we used to develop the package.

#### Install from pip
```sh
uv init measurement_name
cd measurement_name
uv add qimchi
```
This method should automatically generate a virtual environment and install the package with all its dependencies. To add more packages to the current measurement / project, you can use the `uv add` command. For example, to add `qcodes` to the current project, run:
```sh
uv add qcodes
```
`uv` automatically creates and manages the virtual environment for you.

#### Development install
```sh
git clone https://gitlab.com/squad-lab/qimchi.git
cd qimchi
uv add --dev .
```
This makes and installs qimchi in a virtual environment with all dependencies. If you would like to manually manage the virtual environment, you need to activate it.

#### Activate the environment
On MacOS or Linux
```sh
source .venv/bin/activate
```
Or for windows:
```powershell
.venv\Scripts\activate
```

### With pip
> ☀️ **ALTERNATE METHOD** ☀️

If you prefer `pip` for a more traditional installation, you can install dependencies manually, but we strongly recommend following the `uv` installation method above for better performance and dependency management.

#### Clone the repository
```sh
git clone https://github.com/squad-lab/qimchi.git
cd qimchi
```

#### Create and activate a virtual environment
On MacOS or Linux
```sh
python3 -m venv .venv
source .venv/bin/activate
```
Or for windows:
```powershell
python3 -m venv .venv
.venv\Scripts\activate
```

#### Install the package
```sh
pip install -e .
```

## Run Qimchi
Running qimchi is easy, after installing it in a suitable environment:

### With uv
```sh
uv run -m qimchi
```

### With base python
After activating the virtual environment, you can run the package with:
```sh
python -m qimchi
```

## Measurements
An example measurement for testing the package is included as `measure.py`. Running this requires `qcutils`, our own measurement framework. An example measurement is included in the `test` directory.