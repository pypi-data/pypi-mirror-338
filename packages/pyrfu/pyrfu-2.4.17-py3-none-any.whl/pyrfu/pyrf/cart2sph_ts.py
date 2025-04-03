#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3rd party imports
import numpy as np
import xarray as xr

# Local imports
from .ts_vec_xyz import ts_vec_xyz

__author__ = "Louis Richard"
__email__ = "louisr@irfu.se"
__copyright__ = "Copyright 2020-2023"
__license__ = "MIT"
__version__ = "2.4.2"
__status__ = "Prototype"


def cart2sph_ts(inp, direction_flag: int = 1):
    r"""Computes magnitude, theta and phi angle from column vector xyz
    (first column is x ....) theta is 0 at equator.
    direction_flag = -1  -> to make transformation in opposite direction

    Parameters
    ----------
    inp : xarray.DataArray
        Time series to convert.

    direction_flag : {1, -1}, Optional
        Set to 1 (default) to transform from cartesian to spherical
        coordinates. Set to -1 to transform from spherical to cartesian
        coordinates.

    Returns
    -------
    out : xarray.DataArray
        Input field in spherical/cartesian coordinate system.

    """

    # Check input type
    assert isinstance(inp, xr.DataArray), "inp must be a xarray.DataArray"

    # Check that inp is a vector time series
    assert inp.data.ndim == 2 and inp.shape[1] == 3, "inp must be a vector time series"

    # Check direction +/-1
    assert direction_flag in [-1, 1], "direction_flag must be +/-1"

    if direction_flag == -1:
        r_data = inp.data[:, 0]

        sin_the = np.sin(np.deg2rad(inp.data[:, 1]))
        cos_the = np.cos(np.deg2rad(inp.data[:, 1]))
        sin_phi = np.sin(np.deg2rad(inp.data[:, 2]))
        cos_phi = np.cos(np.deg2rad(inp.data[:, 2]))

        z_data = r_data * sin_the
        x_data = r_data * cos_the * cos_phi
        y_data = r_data * cos_the * sin_phi

        out_data = np.transpose(np.vstack([x_data, y_data, z_data]))

    else:
        xy2 = inp.data[:, 0] ** 2 + inp.data[:, 1] ** 2

        r_data = np.sqrt(xy2 + inp.data[:, 2] ** 2)
        theta = np.rad2deg(np.arctan2(inp.data[:, 2], np.sqrt(xy2)))
        phi = np.rad2deg(np.arctan2(inp.data[:, 1], inp.data[:, 0]))

        out_data = np.transpose(np.vstack([r_data, theta, phi]))

    out = ts_vec_xyz(inp.time.data, out_data, inp.attrs)

    return out
