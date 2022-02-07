import matplotlib.pyplot as plt


def tropo_figure(data_ecmwf, data_metop):
    alt_ecmwf = data_ecmwf.cpt_altitude.values
    temp_ecmwf = data_ecmwf.cpt_temperature.values
    alt_metop = data_metop.cpt_altitude.values
    temp_metop = data_metop.cpt_temperature.values

    fig, axs = plt.subplots(2, constrained_layout=True)

    axs[0].plot(data_ecmwf.temperature, data_ecmwf.altitude, label="ECMWF")
    axs[0].plot(
        temp_ecmwf,
        alt_ecmwf,
        "or",
        label=f"CPT: {alt_ecmwf:.1f} m, {temp_ecmwf:.1f} K",
    )
    axs[0].set(
        title=f"Cold point tropopause: latitude {data_ecmwf.lat_limit.values}, time {data_ecmwf.time.astype('datetime64[M]').values}",
        xlabel="Temperature / K",
        ylabel="Altitude / m",
    )

    axs[1].plot(data_metop.temperature, data_metop.altitude, label="METOP")
    axs[1].plot(
        temp_metop,
        alt_metop,
        "or",
        label=f"CPT: {alt_metop:.1f} m, {temp_metop:.1f} K",
    )
    axs[1].set(
        title=f"Cold point tropopause: latitude {data_metop.lat_limit}, time {data_metop.time_limit[0]}",
        xlabel="Temperature / K",
        ylabel="Altitude / m",
    )
    axs[0].legend()
    axs[1].legend()
    fig.savefig("CPT.png")
