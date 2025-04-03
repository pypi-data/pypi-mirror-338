#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Tuple, Union

import matplotlib.pyplot as plt

# 3rd party imports
import numpy as np
from matplotlib.axes import Axes
from matplotlib.colorbar import Colorbar
from matplotlib.image import AxesImage
from mpl_toolkits.axes_grid1 import make_axes_locatable

__author__ = "Louis Richard"
__email__ = "louisr@irfu.se"
__copyright__ = "Copyright 2020-2023"
__license__ = "MIT"
__version__ = "2.4.2"
__status__ = "Prototype"


def plot_heatmap(
    ax: Axes,
    data: Union[np.ndarray, List[List[float]]],
    row_labels: Union[np.ndarray, List[str]],
    col_labels: Union[np.ndarray, List[str]],
    cbar_kw: dict = None,
    cbarlabel: str = "",
    **kwargs,
) -> Tuple[AxesImage, Colorbar]:
    r"""Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    ax : matplotlib.axes._axes.Axes
        Axis to which the heatmap is plotted.
    data : array_like
        A 2D numpy array of shape (N, M).
    row_labels : list or numpy.ndarray
        A list or array of length N with the labels for the rows.
    col_labels : list or numpy.ndarray
        A list or array of length M with the labels for the columns.
    cbar_kw : dict, Optional
        A dictionary with arguments to `matplotlib.Figure.colorbar`.
    cbarlabel : str, Optional
        The label for the colorbar.
    **kwargs
        All other arguments are forwarded to `imshow`.

    Returns
    -------
    im : matplotlib.image.AxesImage
        The AxesImage of the data.
    cbar : matplotlib.colorbar.Colorbar
        Colorbar.

    """
    if ax is None:
        _, ax = plt.subplots(1)

    if not isinstance(data, (list, np.ndarray)):
        raise TypeError("row_labels must be a list or numpy.ndarray")

    if not isinstance(row_labels, (list, np.ndarray)):
        raise TypeError("row_labels must be a list or numpy.ndarray")

    if not isinstance(col_labels, (list, np.ndarray)):
        raise TypeError("col_labels must be a list or numpy.ndarray")

    if data.shape[0] != len(row_labels):
        raise ValueError("row_labels must have the same length as data")

    if data.shape[1] != len(col_labels):
        raise ValueError("col_labels must have the same length as data")

    # Plot the heatmap
    if cbar_kw is None:
        cbar_kw = {}

    im = ax.imshow(data, **kwargs)

    divider = make_axes_locatable(ax)

    colorbar_axes = divider.append_axes("right", size="2%", pad=0.1)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, cax=colorbar_axes, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel)

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=True, labeltop=True, labelbottom=False)

    # Turn spines off and create white grid.
    # ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1] + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0] + 1) - 0.5, minor=True)
    ax.grid(which="minor", color="k", linestyle="-", linewidth=0.5)
    ax.tick_params(which="minor", bottom=False, left=False)
    ax.set_axisbelow(False)
    cbar.ax.set_axisbelow(False)

    return im, cbar
