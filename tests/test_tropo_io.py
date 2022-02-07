import xarray as xr
from tropopause import tropo_io


def test_io_gridded():
    assert type(tropo_io.read_ecmwf()) == type(xr.Dataset())


def test_io_index_based():
    assert type(tropo_io.read_metop()) == type(xr.Dataset())
