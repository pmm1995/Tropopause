import argparse
import datetime

from . import tropo_calc
from . import tropo_io
from .tropo_figure import tropo_figure


def cpt():
    """Upper and lower boundary for the calculation of the cold point tropopause"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lat",
        required=True,
        nargs="+",
        type=int,
        help="Type in two integers for upper and lower boundary of the latitude range",
    )
    parser.add_argument(
        "--time",
        required=False,
        type=lambda s: datetime.datetime.strptime(s, "%Y-%m"),
        default="2020-12",
        help="Type in the time for the tropopause calculation. Format: YYYY-MM (default: 2020-12)",
        metavar="YYYY-MM",
    )

    args = parser.parse_args()

    data_ecmwf = tropo_calc.cpt_from_gridded(tropo_io.read_ecmwf(), args.lat, args.time)
    data_metop = tropo_calc.cpt_from_index_based(tropo_io.read_metop(), args.lat)
    tropo_figure(data_ecmwf, data_metop)
