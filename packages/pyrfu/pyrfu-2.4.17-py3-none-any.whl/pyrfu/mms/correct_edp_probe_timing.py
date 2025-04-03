#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3rd party imports
import numpy as np
import xarray as xr

# Local imports
from ..pyrf.resample import resample
from ..pyrf.ts_scalar import ts_scalar

__author__ = "Louis Richard"
__email__ = "louisr@irfu.se"
__copyright__ = "Copyright 2020-2023"
__license__ = "MIT"
__version__ = "2.4.2"
__status__ = "Prototype"


def correct_edp_probe_timing(sc_pot):
    r"""Corrects for the channel delays not accounted for in the MMS EDP
    processing. As described in the MMS EDP data products guide.

    Parameters
    ----------
    sc_pot : xarray.DataArray
        Time series created from L2 sc_pot files, from the variable
        "mms#_edp_dcv_brst_l2" containing individual probe potentials.

    Returns
    -------
    v_corrected : xarray.DataArray
        Time series where the channel delay for each probe have been
        accounted and corrected for.

    Notes
    -----
    This function is only useful for Burst mode data. For the other
    telemetry modes (i.e. slow and fast) the channel delays are
    completely negligible and the interpolation and resampling applied
    here will have no effect other than possibly introduce numerical
    noise.

    """

    e_fact = [0.1200, 0.1200, 0.0292]

    # Reconstruct E12, E34, E56 as computed in MMS processing
    time = sc_pot.time.data

    diff_sc_pot = []
    for i, fact in zip([0, 2, 4], e_fact):
        diff_sc_pot.append(
            ts_scalar(time, np.diff(sc_pot.data[:, i : i + 2]) / fact),
        )

    # Correct the time tags to create individual time series
    tau_vs = [
        np.timedelta64(0, "ns"),
        np.timedelta64(7629, "ns"),
        np.timedelta64(15259, "ns"),
    ]
    tau_es = [
        np.timedelta64(26703, "ns"),
        np.timedelta64(30518, "ns"),
        np.timedelta64(34332, "ns"),
    ]

    # Odds probes potential 1, 3, 5
    sc_pot_odds = []
    for tau, i in zip(tau_vs, [0, 2, 4]):
        sc_pot_odds.append(ts_scalar(time + tau, sc_pot.data[:, i]))

    # Electric field
    diff_sc_pot = []
    for e_, tau in zip(diff_sc_pot, tau_es):
        diff_sc_pot.append(ts_scalar(e_.time.data + tau, e_.data))

    # Resample all data to time tags of V1 (i.e. timeOrig).
    sc_pot_odds = [resample(v, sc_pot) for v in sc_pot_odds]
    diff_sc_pot = [resample(e, sc_pot) for e in diff_sc_pot]

    # Recompute individual even probe potentials 2, 4, 6
    sc_pot_even = []
    for v_, e_, fact in zip(sc_pot_odds, diff_sc_pot, e_fact):
        sc_pot_even.append(v_ - e_ * fact)

    sc_pot_corrected = []
    for tup in zip(sc_pot_even, sc_pot_odds):
        for item in tup:
            sc_pot_corrected.append(item.data)

    # Create the new time series with the corrected values
    options = {"coords": [time, np.arange(1, 7)], "dims": ["time", "probe"]}
    sc_pot_corrected = xr.DataArray(sc_pot_corrected, **options)

    return sc_pot_corrected
