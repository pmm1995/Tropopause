# Cold point tropopause

## Peter Müller (01613871)
This installable python module calculates the cold point tropopause (CPT) of two different data sets:
1) ECMWF ERA5 reanalysis
2) European METOP-satellite

The module was developed within the course "411.045 Selected Topics in Climate Science (Python for climate and environmental scientists)"
during the winter semester 2021/22 at the KFU Graz.

The structure of this installable program is based on the "Minimal example" created by Florian 
Ladstädter (https://gitlab.com/flad/minimal_example/).

The package provides a shell script `cpt` with the required arguments:
- `--lat`: Two integers as the lower and upper boundaries of the latitude interval of interest.

Additionally also the desired month (working only for the ECMWF data) can be specified:
- `--time`: Specify the month of the measurement to be an analyzed. Format YYYY-MM. Default: 2020-12

The METOP file only provides data for 2020-01.

For further information type `tropopause --help`.

## Installation
The creation of a virtual environment is not necessary but recommende to have an isolated system
to test the application. In this case the virtul environment needs to be activated
before the installation.

```bash
conda create --name mynewenv python
conda activate mynewenv
```

Use the following command in the base directory to install:
```bash
python -m pip install .
```
For an editable ("developer mode") installation, use the following
instead:

```bash
python -m pip install -e .
```

With this, the installation is actually a link to the original source code,
i.e. each change in the source code is immediately available.

## Previous requirements
A working Python environment is needed and `pip` needs to be installed.
This can be done, for example, using `conda`:
```bash
conda create --name mynewenv python
conda activate mynewenv
python -m pip install -e .
```

The module requires:
1) `xarray`
2) `numpy`
3) `matplotlib`