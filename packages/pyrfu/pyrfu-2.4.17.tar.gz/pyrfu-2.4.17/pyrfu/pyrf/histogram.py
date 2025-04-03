#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3rd party imports
import numpy as np
import xarray as xr

__author__ = "Louis Richard"
__email__ = "louisr@irfu.se"
__copyright__ = "Copyright 2020-2023"
__license__ = "MIT"
__version__ = "2.4.2"
__status__ = "Prototype"


def histogram(inp, bins=100, y_range=None, weights=None, density=True):
    r"""Computes 1D histogram of the inp with bins bins

    Parameters
    ----------
    inp : xarray.DataArray
        Time series of the input scalar variable.
    bins : str or int or array_like, Optional
        Number of bins. Default is ``bins=100``.
    y_range : (float, float), Optional
        The lower and upper range of the bins.  If not provided, range
        is simply ``(inp.min(), inp.max())``.  Values outside the range are
        ignored. The first element of the range must be less than or
        equal to the second. `range` affects the automatic bin
        computation as well. While bin width is computed to be optimal
        based on the actual data within `range`, the bin count will fill
        the entire range including portions containing no data.
    weights : array_like, Optional
        An array of weights, of the same shape as `inp`.  Each value in
        `inp` only contributes its associated weight towards the bin count
        (instead of 1). If `density` is True, the weights are
        normalized, so that the integral of the density over the range
        remains 1.
    density : bool, Optional
        If ``False``, the result will contain the number of samples in each
        bin. If ``True``, the result is the value of the probability *density*
        function at the bin, normalized such that the *integral* over the
        range is 1. Note that the sum of the histogram values will not be
        equal to 1 unless bins of unity width are chosen; it is not a
        probability mass function.

    Returns
    -------
    out : xarray.DataArray
        1D distribution of the input time series.

    """

    # Check input
    assert isinstance(inp, xr.DataArray), "inp must be a xarray.DataArray"
    assert inp.ndim == 1, "inp must be a scalar time series"

    hist, bins = np.histogram(
        inp.data,
        bins=bins,
        range=y_range,
        weights=weights,
        density=density,
    )
    bin_center = (bins[1:] + bins[:-1]) * 0.5

    out = xr.DataArray(hist, coords=[bin_center], dims=["bins"])

    return out
