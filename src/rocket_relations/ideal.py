"""
ideal.py
========

The functions in this module assume ideal gas behavior and isentropic,
adiabatic flow through a converging-diverging nozzle. They accept scalars or
NumPy arrays as inputs in standard SI Units:

- gamma (ratio of specific heats) must be > 1 and < 1.8
- Pressure ratios must be in [0, 1)
- Nozzle area ratio must be >= 1
- Stagnation temperature must be > 0
- Specific gas constant must be > 0

Functions
---------

- :func:`solve_cstar` - Computes the characteristic velocity (c*) for a given gas.
- :func:`solve_cf` - Computes the thrust coefficient (C_f) for a choked nozzle.

"""

import numpy as np

def solve_cstar(gamma, Rs, T0):
    """
    Compute the characteristic velocity c* for a given gas.

    :param gamma: Ratio of specific heats (dimensionless, must be > 1 and < 1.8).
    :type gamma: float or numpy.ndarray
    :param Rs: Specific gas constant [J/(kg*K)] (must be > 0).
    :type Rs: float or numpy.ndarray
    :param T0: Stagnation temperature [K] (must be > 0).
    :type T0: float or numpy.ndarray

    :return: Characteristic velocity [m/s].
    :rtype: numpy.ndarray

    :raises TypeError: If any input is non-numeric.
    :raises ValueError: If inputs violate physical domain constraints.
    """
    for name, value in {"gamma": gamma, "Rs": Rs, "T0": T0}.items():
        if not np.issubdtype(np.array(value).dtype, np.number):
            raise TypeError(f"{name} must be numeric")

    gamma = np.asarray(gamma, dtype=float)
    Rs = np.asarray(Rs, dtype=float)
    T0 = np.asarray(T0, dtype=float)

    if np.any(gamma <= 1) or np.any(gamma >= 1.8):
        raise ValueError("gamma must be > 1 and < 1.8")
    if np.any(Rs <= 0):
        raise ValueError("Specific gas constant must be > 0")
    if np.any(T0 <= 0):
        raise ValueError("Stagnation temperature must be > 0")

    return np.sqrt((1 / gamma) * ((gamma + 1) / 2) ** ((gamma + 1) / (gamma - 1)) * Rs * T0)


def solve_cf(gamma, ratio_pe_p0, ratio_pa_p0, ratio_Ae_Astar):
    """
    Compute the thrust coefficient C_f for a rocket nozzle.

    :param gamma: Ratio of specific heats (dimensionless, must be > 1 and < 1.8).
    :type gamma: float or numpy.ndarray
    :param ratio_pe_p0: Exit to stagnation pressure ratio (dimensionless, must be in [0, 1)).
    :type ratio_pe_p0: float or numpy.ndarray
    :param ratio_pa_p0: Ambient to stagnation pressure ratio (dimensionless, must be in [0, 1)).
    :type ratio_pa_p0: float or numpy.ndarray
    :param ratio_Ae_Astar: Exit to throat area ratio (dimensionless, must be >= 1).
    :type ratio_Ae_Astar: float or numpy.ndarray

    :return: Thrust coefficient C_f (dimensionless).
    :rtype: numpy.ndarray

    :raises TypeError: If any input is non-numeric.
    :raises ValueError: If inputs violate physical domain constraints.
    """
    inputs = {
        "gamma": gamma,
        "ratio_pe_p0": ratio_pe_p0,
        "ratio_pa_p0": ratio_pa_p0,
        "ratio_Ae_Astar": ratio_Ae_Astar
    }
    for name, value in inputs.items():
        if not np.issubdtype(np.array(value).dtype, np.number):
            raise TypeError(f"{name} must be numeric")

    gamma = np.asarray(gamma, dtype=float)
    ratio_pe_p0 = np.asarray(ratio_pe_p0, dtype=float)
    ratio_pa_p0 = np.asarray(ratio_pa_p0, dtype=float)
    ratio_Ae_Astar = np.asarray(ratio_Ae_Astar, dtype=float)

    if np.any(gamma <= 1) or np.any(gamma >= 1.8):
        raise ValueError("gamma must be > 1 and < 1.8")
    if np.any((ratio_pe_p0 < 0) | (ratio_pe_p0 >= 1)):
        raise ValueError("ratio_pe_p0 must be in [0, 1)")
    if np.any((ratio_pa_p0 < 0) | (ratio_pa_p0 >= 1)):
        raise ValueError("ratio_pa_p0 must be in [0, 1)")
    if np.any(ratio_Ae_Astar < 1):
        raise ValueError("ratio_Ae_Astar must be >= 1")

    return np.sqrt(
        (2 * gamma**2 / (gamma - 1))
        * (2 / (gamma + 1)) ** ((gamma + 1) / (gamma - 1))
        * (1 - ratio_pe_p0 ** ((gamma - 1) / gamma))
        + (ratio_pe_p0 - ratio_pa_p0) * ratio_Ae_Astar
    )
