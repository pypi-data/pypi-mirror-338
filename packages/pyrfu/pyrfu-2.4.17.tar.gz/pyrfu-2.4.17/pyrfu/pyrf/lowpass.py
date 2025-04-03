#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3rd party imports
import xarray as xr
from scipy import signal

__author__ = "Louis Richard"
__email__ = "louisr@irfu.se"
__copyright__ = "Copyright 2020-2023"
__license__ = "MIT"
__version__ = "2.4.2"
__status__ = "Prototype"


def lowpass(inp, f_cut, fhz):
    r"""Filter the data through low or highpass filter with max
    frequency f_cut and subtract from the original.

    Parameters
    ----------
    inp : xarray.DataArray
        Time series of the input variable.
    f_cut : float
        Cutoff frequency.
    fhz : float
        Sampling frequency.

    Returns
    -------
    out : xarray.DataArray
        Time series of the filter data.

    """

    data = inp.data

    # Remove trend
    data_detrend = signal.detrend(data, type="linear", axis=0)
    rest = data - data_detrend

    # Elliptic filter
    f_nyq, r_pass, r_stop, order = [fhz / 2, 0.1, 60, 4]

    elliptic_filter = signal.ellip(
        order,
        r_pass,
        r_stop,
        f_cut / f_nyq,
        output="ba",
    )

    # Filter data
    out_data = signal.filtfilt(
        elliptic_filter[0],
        elliptic_filter[1],
        data_detrend,
        axis=0,
    )

    out = xr.DataArray(out_data + rest, coords=inp.coords, dims=inp.dims)

    return out
