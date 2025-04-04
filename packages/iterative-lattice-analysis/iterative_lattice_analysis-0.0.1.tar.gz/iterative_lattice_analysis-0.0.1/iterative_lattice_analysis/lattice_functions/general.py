import typing
import math
import numpy as np
import sympy
import scipy
from PyTPSA.tpsa import tpsa
from PyTPSA.tpsa import sin as sin_tpsa
from PyTPSA.tpsa import cos as cos_tpsa
from PyTPSA.tpsa import tan as tan_tpsa
from ..support_functions import sympy_tpsa_numpy_trig


def linear_matrix_2D(
    beta1: np.float64,
    alpha1: np.float64,
    beta2: np.float64,
    alpha2: np.float64,
    phase: np.float64,
) -> np.ndarray:
    sphi = math.sin(phase)
    cphi = math.cos(phase)
    sqrtb1b2 = math.sqrt(beta1 * beta2)

    m00 = math.sqrt(beta2 / beta1) * (cphi + alpha1 * sphi)
    m01 = sqrtb1b2 * sphi
    m10 = (-(1 + alpha1 * alpha2) * sphi + (alpha1 - alpha2) * cphi) / sqrtb1b2
    m11 = math.sqrt(beta1 / beta2) * (cphi - alpha2 * sphi)

    m = np.array([[m00, m01], [m10, m11]], dtype=np.float64)

    return m


def linear_matrix_4D(
    betax1: np.float64,
    alphax1: np.float64,
    betax2: np.float64,
    alphax2: np.float64,
    betay1: np.float64,
    alphay1: np.float64,
    betay2: np.float64,
    alphay2: np.float64,
    mux: np.float64,
    muy: np.float64,
) -> np.ndarray:
    dim = 4
    M = np.eye(dim, dtype=np.float64)
    Mx = linear_matrix_2D(betax1, alphax1, betax2, alphax2, mux)
    My = linear_matrix_2D(betay1, alphay1, betay2, alphay2, muy)

    M[: dim // 2, : dim // 2] = Mx
    M[dim // 2 :, dim // 2 :] = My

    return M


def linear_element(
    x: np.float64, px: np.float64, y: np.float64, py: np.float64, M: np.ndarray
) -> typing.Tuple[np.float64, np.float64, np.float64, np.float64]:
    X = np.array([x, px, y, py])

    nX = np.matmul(M, X, dtype=type(x))

    nx = nX[0]
    npx = nX[1]
    nz = nX[2]
    npz = nX[3]

    return nx, npx, nz, npz


def longitudinal_element(
    z: np.float64,
    pz: np.float64,
    energy: np.float64,
    charge: int,
    phi_s: np.float64,
    rf_voltage: np.float64,
    harmonic_number: int,
    slip_factor: np.float64,
    beta_s: np.float64,
    rf_frequency: np.float64,
) -> typing.Tuple[np.float64, np.float64]:
    """
    Simple standard map like function for the longitudinal dynamics.
    """
    # voltate in V
    # energy in eV

    phi = phi_s - rf_frequency * z / beta_s / scipy.constants.c

    sin_phi = sympy_tpsa_numpy_trig(phi, trig_functions=["sin"])[0]

    npz = pz + (sin_phi - math.sin(phi_s)) * charge * rf_voltage / (energy * beta_s**2)
    nz = (
        z
        - 2
        * np.pi
        * harmonic_number
        * beta_s
        * scipy.constants.c
        * slip_factor
        * npz
        / rf_frequency
    )

    return nz, npz
