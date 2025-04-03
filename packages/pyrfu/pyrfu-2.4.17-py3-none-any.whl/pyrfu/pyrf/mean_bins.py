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


def mean_bins(inp0, inp1, bins: int = 10):
    r"""Computes mean of values of y corresponding to bins of x.

    Parameters
    ----------
    inp0 : xarray.DataArray
        Time series of the quantity of corresponding to the bins.
    inp1 : xarray.DataArray
        Time series of the quantity to compute the binned mean.
    bins : int, Optional
        Number of bins.

    Returns
    -------
    out : xarray.Dataset
        Dataset with :
            * bins : xarray.DataArray
                bin values of the x variable.
            * data : xarray.DataArray
                Mean values of y corresponding to each bin of x.
            * sigma : xarray.DataArray
                Standard deviation.

    Examples
    --------
    >>> import numpy
    >>> from pyrfu import mms, pyrf

    Time interval

    >>> tint = ["2019-09-14T07:54:00.000", "2019-09-14T08:11:00.000"]

    Spacecraft indices

    >>> mms_list = numpy.arange(1,5)

    Load magnetic field and electric field

    >>> r_mms, b_mms = [[] * 4 for _ in range(2)]
    >>> for mms_id in range(1, 5):
    >>> 	r_mms.append(mms.get_data("R_gse", tint, mms_id))
    >>> 	b_mms.append(mms.get_data("B_gse_fgm_srvy_l2", tint, mms_id))
    >>>

    Compute current density, etc

    >>> j_xyz, _, b_xyz, _, _, _ = pyrf.c_4_j(r_mms, b_mms)

    Compute magnitude of B and J

    >>> b_mag = pyrf.norm(b_xyz)
    >>> j_mag = pyrf.norm(j_xyz)

    Mean value of J for 10 bins of B

    >>> m_b_j = pyrf.mean_bins(b_mag, j_mag)

    """

    assert isinstance(inp0, xr.DataArray), "inp0 must be xaray.DataArray"
    assert isinstance(inp1, xr.DataArray), "inp1 must be xaray.DataArray"

    assert inp0.ndim == 1, "inp0 must be a scalar"
    assert inp1.ndim == 1, "inp1 must be a scalar"

    x_sort = np.sort(inp0.data)
    x_edge = np.linspace(x_sort[0], x_sort[-1], bins + 1)

    y_avg, y_std = [np.zeros(bins), np.zeros(bins)]

    for i in range(bins):
        idx_left = inp0.data > x_edge[i]
        idx_right = inp0.data < x_edge[i + 1]

        y_bins = inp1.data[idx_left * idx_right]

        y_avg[i], y_std[i] = [np.mean(y_bins), np.std(y_bins)]

    bins = x_edge[:-1] + np.median(np.diff(x_edge)) / 2

    out_dict = {
        "data": (["bins"], y_avg),
        "sigma": (["bins"], y_std),
        "bins": bins,
    }

    out = xr.Dataset(out_dict)

    return out
