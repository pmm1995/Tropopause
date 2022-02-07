import numpy as np


def _cpt_calc(ds):
    temp = ds.temperature.sel(altitude=slice(5000, 20000))
    ds["cpt_temperature"] = temp.min()
    ds["cpt_altitude"] = temp.idxmin()
    return ds


def cpt_from_gridded(ds, lat, time):

    t = time

    ds_sel = (
        ds.sel(latitude=slice(lat[0], lat[1]))
        .sel(time=t, method="nearest")
        .mean(dim="longitude")
    )
    lat_limit = [
        ds_sel.latitude_bounds.values.min(),
        ds_sel.latitude_bounds.values.max(),
    ]
    ds_sel = ds_sel.mean(dim="latitude", keep_attrs=True)
    ds_sel["lat_limit"] = lat_limit

    ds_sel = _cpt_calc(ds_sel)

    return ds_sel


def cpt_from_index_based(ds, lat):
    ds_sel = ds.where(ds.latitude >= lat[0], drop=True)
    ds_sel = ds_sel.where(ds_sel.latitude <= lat[1], drop=True)

    lat_limit = (
        np.round(ds_sel.latitude.values.min(), 1),
        np.round(ds_sel.latitude.values.max(), 1),
    )

    time_limit = [
        ds_sel.time.values.min().astype("datetime64[M]").astype("str"),
        ds_sel.time.values.max().astype("datetime64[M]").astype("str"),
    ]
    ds_sel = ds_sel.mean("n_event")
    ds_sel.attrs["lat_limit"] = lat_limit
    ds_sel.attrs["time_limit"] = time_limit
    ds_sel.attrs["cpt_temperature"] = ds_sel.temperature.min()
    ds_sel.attrs["cpt_altitude"] = ds_sel.temperature.idxmin()

    return ds_sel
