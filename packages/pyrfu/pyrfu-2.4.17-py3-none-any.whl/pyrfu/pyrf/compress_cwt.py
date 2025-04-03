#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3rd party import
import numba
import numpy as np
import xarray as xr

__author__ = "Louis Richard"
__email__ = "louisr@irfu.se"
__copyright__ = "Copyright 2020-2023"
__license__ = "MIT"
__version__ = "2.4.2"
__status__ = "Prototype"


@numba.jit(cache=True, fastmath=True, nopython=True, parallel=True)
def _compress_cwt_1d(cwt, nc: int = 100):
    nf = cwt.shape[1]
    idxs = np.arange(
        int(nc / 2),
        len(cwt) - int(nc / 2),
        step=nc,
        dtype=np.int64,
    )
    cwt_c = np.zeros((len(idxs), nf))

    for i, idx in enumerate(idxs):
        for j in range(nf):
            x_data = cwt[idx - int(nc / 2) : idx + int(nc / 2), j]
            cwt_c[i, j] = np.nanmean(x_data)

    return cwt_c


def compress_cwt(cwt, nc: int = 100):
    r"""Compress the wavelet transform averaging of nc time steps.

    Parameters
    ----------
    cwt : xarray.Dataset
        Wavelet transform to compress.
    nc : int, Optional
        Number of time steps for averaging. Default is 100.

    Returns
    -------
    cwt_t : xarray.DataArray
        Sampling times.
    cwt_x : ndarray
        Compressed wavelet transform of the first component of the field.
    cwt_y : ndarray
        Compressed wavelet transform of the second component of the field.
    cwt_z : ndarray
        Compressed wavelet transform of the third component of the field.

    """

    assert isinstance(cwt, xr.Dataset), "cwt must be an xarray.Dataset"

    indices = np.arange(
        int(nc / 2),
        len(cwt.time.data) - int(nc / 2),
        step=nc,
        dtype=np.int64,
    )

    cwt_t = cwt.time.data[indices]
    cwt_x = _compress_cwt_1d(cwt.x.data, nc=nc)
    cwt_y = _compress_cwt_1d(cwt.y.data, nc=nc)
    cwt_z = _compress_cwt_1d(cwt.z.data, nc=nc)

    return cwt_t, cwt_x, cwt_y, cwt_z
