import os

import xarray as xr
from pkg_resources import resource_filename

file_ecmwf = resource_filename(
    __name__,
    os.path.join(
        "data",
        "ECMWF_IFS-ea-0051_an_F32-T42_yggdrasil-0.5.0_altitude_10x10_temperature.nc",
    ),
)

file_metop = resource_filename(
    __name__,
    os.path.join("data", "METOP-A_GPS_2020-01-01_OPSv5.6.2_UCAR-2016.0120_L2.nc",),
)


def read_ecmwf():
    """Opens the ECMWF datafile and reads it into memory"""
    with xr.open_dataset(file_ecmwf) as ds:
        ds.load()
    print(type(ds))
    return ds


def read_metop():
    """Opens the METOP datafile and reads it into memory"""
    with xr.open_dataset(file_metop) as ds:
        ds.load()
    return ds
