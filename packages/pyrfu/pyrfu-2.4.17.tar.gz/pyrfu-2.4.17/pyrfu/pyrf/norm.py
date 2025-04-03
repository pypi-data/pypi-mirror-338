#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3rd party imports
import numpy as np

# Local imports
from .ts_scalar import ts_scalar

__author__ = "Louis Richard"
__email__ = "louisr@irfu.se"
__copyright__ = "Copyright 2020-2023"
__license__ = "MIT"
__version__ = "2.4.2"
__status__ = "Prototype"


def norm(inp):
    r"""Computes the magnitude of the input field.

    Parameters
    ----------
    inp : xarray.DataArray
        Time series of the input field.

    Returns
    -------
    out : xarray.DataArray
        Time series of the magnitude of the input field.

    Examples
    --------
    >>> from pyrfu import mms, pyrf

    Time interval

    >>> tint = ["2019-09-14T07:54:00.000", "2019-09-14T08:11:00.000"]

    Spacecraft index

    >>> mms_id = 1

    Load magnetic field

    >>> b_xyz = mms.get_data("B_gse_fgm_srvy_l2", tint, mms_id)

    Compute magnitude of the magnetic field

    >>> b_mag = pyrf.norm(b_xyz)

    """

    out = ts_scalar(inp.time.data, np.linalg.norm(inp.data, axis=1), attrs=inp.attrs)

    return out
