import numpy as np
from tropopause import tropo_calc
from tropopause import tropo_io


lat_range = (-20, 20)
time = np.datetime64("2020-12")


def test_tropo_calc_gridded():
    ds = tropo_calc.cpt_from_gridded(tropo_io.read_ecmwf(), lat_range, time)
    assert ds.cpt_temperature.values > 0
    assert ds.cpt_altitude.values > 0
    assert ds.temperature.ndim == 1
    assert ds.altitude.shape == ds.temperature.shape
    assert ds.time.size == 1
    assert ds.lat_limit.size == 2
    assert ds.lat_limit.max() < 180


def test_tropo_calc_index():
    ds = tropo_calc.cpt_from_index_based(tropo_io.read_metop(), lat_range)
    assert ds.cpt_temperature.values > 0
    assert ds.cpt_altitude.values > 0
    assert ds.temperature.ndim == 1
    assert ds.altitude.shape == ds.temperature.shape
    assert len(ds.time_limit) == 2
    assert len(ds.lat_limit) == 2
    assert max(ds.lat_limit) < 180
