#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3rd party imports
import numpy as np
import xarray as xr

# Local imports
from ..pyrf.extend_tint import extend_tint
from ..pyrf.resample import resample
from ..pyrf.time_clip import time_clip
from ..pyrf.ts_scalar import ts_scalar

__author__ = "Louis Richard"
__email__ = "louisr@irfu.se"
__copyright__ = "Copyright 2020-2023"
__license__ = "MIT"
__version__ = "2.4.2"
__status__ = "Prototype"


def probe_align_times(e_xyz, b_xyz, sc_pot, z_phase):
    r"""Returns times when field-aligned electrostatic waves can be
    characterized using interferometry techniques. The same alignment
    conditions as Graham et al., JGR, 2015 are used. Optional figure produced
    showing E_FAC, probe fields, and probe potentials to view time delays
    between electric fields aligned with B.  Currently p5-p6 are not used in
    this routine; the analysis is the same as the one used for Cluster.

    For the figure the panels are :
        * (a) B in DMPA Coordinates
        * (b) Magnitude of B in and out of the spin plane
        * (c) Angles between B and probes 1 and 3 in the spin plane
              (angle between 0 and 90 degrees)
        * (d) Spacecraft potential from probes perpendicular to B
        * (e) E fields from p1-p4 and SC for probes closely aligned with B
        * (f) E in field-aligned coordinates
        * (g) E from probes p1-p2 and p3-p4.


    Parameters
    ----------
    e_xyz : xarray.DataArray
        Electric field in DSL coordinates, brst mode.
    b_xyz : xarray.DataArray
        Magnetic field in DMPA coordinates.
    sc_pot : xarray.DataArray
        L2 Spacecraft potential data. Timing corrections are applied in this
    z_phase : xarray.DataArray
        Spacecraft phase (z_phase). Obtained from ancillary_defatt.

    Returns
    -------
    start_time1 : to fill
        Start times of intervals which satisfy the probe alignment conditions
        for probe combinates p1-p2.
    end_time1 : to fill
        End times of intervals which satisfy the probe alignment conditions
        for probe combinates p1-p2.
    start_time3 : to fill
        Start times of intervals which satisfy the probe alignment conditions
        for probe combinates p3-p4.
    end_time3 : to fill
        End times of intervals which satisfy the probe alignment conditions
        for probe combinates p3-p4.

    """

    # Correct for timing in spacecraft potential data.
    e12 = ts_scalar(
        sc_pot.time.data,
        (sc_pot.data[:, 0] - sc_pot.data[:, 1]) / 0.120,
    )
    e34 = ts_scalar(
        sc_pot.time.data,
        (sc_pot.data[:, 2] - sc_pot.data[:, 3]) / 0.120,
    )
    e56 = ts_scalar(
        sc_pot.time.data,
        (sc_pot.data[:, 4] - sc_pot.data[:, 4]) / 0.0292,
    )

    v_1 = ts_scalar(sc_pot.time.data, sc_pot.data[:, 0])
    v_3 = ts_scalar(
        sc_pot.time.data + np.timedelta64(7629, "ns"),
        sc_pot.data[:, 2],
    )
    v_5 = ts_scalar(
        sc_pot.time.data + np.timedelta64(15259, "ns"),
        sc_pot.data[:, 4],
    )

    e12.time.data += np.timedelta64(26703, "ns")
    e34.time.data += np.timedelta64(30518, "ns")
    e56.time.data += np.timedelta64(34332, "ns")

    v_1, v_3, v_5 = [resample(v, v_1) for v in [v_1, v_3, v_5]]
    e12, e34, e56 = [resample(e, v_1) for e in [e12, e34, e56]]

    v_2 = v_1 - e12 * 0.120
    v_4 = v_3 - e34 * 0.120
    v_6 = v_5 - e56 * 0.0292

    sc_pot = np.hstack(
        [v_1.data, v_2.data, v_3.data, v_4.data, v_5.data, v_6.data],
    )

    sc_pot = xr.DataArray(
        sc_pot,
        coords=[v_1.time.data, np.arange(1, 7)],
        dims=["time", "probe"],
    )

    t_limit = [sc_pot.time.data[0], sc_pot.time.data[-1]]
    t_limit = [np.datetime_as_string(time, "ns") for time in t_limit]

    t_limit_long = extend_tint(t_limit, [-10, 10])

    b_xyz = time_clip(b_xyz, t_limit_long)
    b_xyz = resample(b_xyz, sc_pot)
    e_xyz = resample(e_xyz, sc_pot)

    z_phase = time_clip(z_phase, t_limit_long)

    # Remove repeated z_phase elements
    n_ph = len(z_phase)
    no_repeat = np.ones(n_ph)

    for i in range(1, n_ph):
        if z_phase.time.data[i] > z_phase.time.data[i - 1]:
            if z_phase.data[i] < z_phase.data[i - 1]:
                z_phase.data[i:] += 360.0
        else:
            no_repeat[i] = 0

    z_phase_time = z_phase.time[no_repeat == 1]
    z_phase_data = z_phase.data[no_repeat == 1]

    z_phase = ts_scalar(z_phase_time, z_phase_data)
    z_phase = resample(z_phase, sc_pot)

    # Probe angles in DSL or whatever
    phase_p = []
    for i, j in zip([1, 7, 2, 5], [6, 6, 3, 3]):
        phase_p.append(np.deg2rad(z_phase.data) + i * np.pi / j)

    r_p = [60 * np.array([np.cos(phase), np.sin(phase)]) for phase in phase_p]

    # Calculate angles between probes and direction of B in the spin plane.
    theta_pb = [None] * 4

    for i in [0, 2]:
        theta_pb[i] = r_p[i][:, 0] * b_xyz.data[:, 0] + r_p[i][:, 1] * b_xyz.data[:, 1]
        theta_pb[i] /= np.sqrt(r_p[i][:, 0] ** 2 + r_p[i][:, 1] ** 2)
        theta_pb[i] /= np.sqrt(b_xyz[:, 0] ** 2 + b_xyz[:, 1] ** 2)
        theta_pb[i] = np.arccos(abs(theta_pb[i])) * 180 / np.pi

    theta_pb[1] = theta_pb[0]
    theta_pb[3] = theta_pb[2]

    sc_v12 = (sc_pot.data[:, 0] + sc_pot.data[:, 1]) / 2
    sc_v34 = (sc_pot.data[:, 2] + sc_pot.data[:, 3]) / 2

    e_s = [None] * 4

    e_s[0] = (sc_pot.data[:, 0] - sc_v34) * 1e3 / 60
    e_s[1] = (sc_v34 - sc_pot.data[:, 0]) * 1e3 / 60
    e_s[2] = (sc_pot.data[:, 2] - sc_v12) * 1e3 / 60
    e_s[3] = (sc_v12 - sc_pot.data[:, 2]) * 1e3 / 60

    e12 = (sc_pot.data[:, 0] - sc_pot.data[:, 1]) * 1e3 / 120
    e34 = (sc_pot.data[:, 2] - sc_pot.data[:, 3]) * 1e3 / 120

    idx_b = np.sqrt(b_xyz.data[:, 0] ** 2 + b_xyz.data[:, 1] ** 2) < abs(
        b_xyz.data[:, 2],
    )
    thresh_ang = 25.0

    for e_, theta in zip(e_s, theta_pb):
        e_[theta > thresh_ang] = np.nan
        e_[idx_b] = np.nan

    sc_v12[theta_pb[2] > thresh_ang] = np.nan
    sc_v34[theta_pb[0] > thresh_ang] = np.nan

    sc_v12[idx_b] = np.nan
    sc_v34[idx_b] = np.nan
