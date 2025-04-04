import math
import typing
import numpy as np
import scipy.constants as const
from . import general
from .. import support_functions

# * Crab Cavity Parameters

# * Transverse beta functions
betax_cc1 = 1300  # [m]
alphax_cc1 = 0

betax_cc2 = 1300  # [m]
alphax_cc2 = 0

betax_ip = 90e-2  # [m]
alphax_ip = 0

# * Beam parameters
sigma_z = 7e-2  # [m]
sigma_zp = 6.6e-4  # [1]
sigma_x = 120e-6  # [m]
sigma_xp = sigma_x / betax_ip  # [1]

# * Longitudinal parameters
energy = 275e9  # [eV]
mass = 938.271998e6  # [eV] # proton
charge = 1  # [e]
phi_s = 0  # [rad]
rf_voltage = 15.8e6  # [V]
rf_frequency = 591e6  # [Hz]
circumference = 3833.8  # [m]
gamma = energy / mass
beta_s = math.sqrt(1 - 1 / gamma**2)
momentum_compaction = 1.5e-3
slip_factor = 1 / gamma**2 - momentum_compaction
harmonic_number = 7560
revolution_frequency = rf_frequency / harmonic_number
# angular_frequency = 2 * np.pi * beta_s * const.c / circumference

# * Longitudinal beta functions
betaz_ip = sigma_z / sigma_zp  # sigma_z / delta_p
alphaz_ip = 0

# Crab cavity parameters
phase_cc = np.pi / 2
fc = 197e6  # Hz
kc = 2 * np.pi * fc / const.c  # [1/m]
theta = 25e-3 / 2  # rad    Half crossing angle

# Normalize magnet strengths for crab cavity (b_n / (B rho)) [b_n] = [Tm/m**(n-1)]
default_sextupole_integrated_strength = 4.412e2 * 1e-3  # [1/m**2]
# default_sextupole_integrated_strength = 0
default_quadrupole_integrated_strength = 3.542e-5 * 1e-3  # [1/m]
# default_sextupole_integrated_strength = 0

xtune = 0.310  # Phase for ip to ip
ztune = 0.015  # 0.01
mux = 2 * np.pi * xtune
muz = 2 * np.pi * ztune
spacial_dim = 2


# Matrices
# ip_to_ip = general.linear_matrix_4D(
#     betax_ip,
#     alphax_ip,
#     betax_ip,
#     alphax_ip,
#     betaz_ip,
#     alphaz_ip,
#     betaz_ip,
#     alphaz_ip,
#     mux,
#     muz,
# )
ip_to_ip = np.eye(2 * spacial_dim, dtype=np.float64)
ip_to_ip[0:spacial_dim, 0:spacial_dim] = general.linear_matrix_2D(
    betax_ip, alphax_ip, betax_ip, alphax_ip, mux
)

# ip_to_cc2 = general.linear_matrix_4D(
#     betax_ip,
#     alphax_ip,
#     betax_cc2,
#     alphax_cc2,
#     betaz_ip,
#     alphaz_ip,
#     betaz_ip,
#     alphaz_ip,
#     phase_cc,
#     0,
# )
ip_to_cc2 = np.eye(2 * spacial_dim, dtype=np.float64)
ip_to_cc2[0:spacial_dim, 0:spacial_dim] = general.linear_matrix_2D(
    betax_ip, alphax_ip, betax_cc2, alphax_cc2, phase_cc
)

# ip_to_cc1_inv = general.linear_matrix_4D(
#     betax_cc1,
#     alphax_cc1,
#     betax_ip,
#     alphax_ip,
#     betaz_ip,
#     alphaz_ip,
#     betaz_ip,
#     alphaz_ip,
#     phase_cc,
#     0,
# )
ip_to_cc1_inv = np.eye(2 * spacial_dim, dtype=np.float64)
ip_to_cc1_inv[0:spacial_dim, 0:spacial_dim] = general.linear_matrix_2D(
    betax_cc1, alphax_cc1, betax_ip, alphax_ip, phase_cc
)

ip_to_cc1 = np.linalg.inv(ip_to_cc1_inv)
ip_to_cc2_inv = np.linalg.inv(ip_to_cc2)


# * Functions
def nonlinear_element(
    x: np.float64,
    px: np.float64,
    z: np.float64,
    pz: np.float64,
) -> typing.Tuple[np.float64, np.float64, np.float64, np.float64]:
    # * Henon
    # cphi1 = np.cos(mux)
    # sphi1 = np.sin(mux)
    # cphi2 = np.cos(muz)
    # sphi2 = np.sin(muz)
    # pxm, pzm, nx, npx, nz, npz

    # pxm = px - x*x + z*z
    # pzm = pz + 2*x*z
    # npx = -x*sphi1 + pxm*cphi1
    # npz = -z*sphi2 + pzm*cphi2
    # nx = x*cphi1 + pxm*sphi1
    # nz = z*cphi2 + pzm*sphi2
    # * End Henon

    # * None
    nx = x
    npx = px
    nz = z
    npz = pz
    # * End None

    return nx, npx, nz, npz


# * Crab Cavity Function


def crab_cavity(
    x: np.float64,
    px: np.float64,
    z: np.float64,
    pz: np.float64,
    beta_cc: np.float64,
    beta_ip: np.float64,
    theta_c: np.float64,
    integrated_magnet_strengths: typing.List[np.float64],
) -> typing.Tuple[np.float64, np.float64, np.float64, np.float64]:
    sqrtbb = np.sqrt(beta_cc * beta_ip)
    ttc = np.tan(theta_c)

    quadrupole_integrated_strength, sextupole_integrated_strength = (
        integrated_magnet_strengths
    )

    # ! Time dependent
    skz, ckz = support_functions.sympy_tpsa_numpy_trig(
        kc * z, trig_functions=["sin", "cos"]
    )

    dpx = -ttc * skz / (kc * sqrtbb)
    dpx += skz * quadrupole_integrated_strength * x  # Quadrupole kick
    dpx += skz * sextupole_integrated_strength * x * x  # Sextupole kick

    dpz = -x * ttc * ckz / sqrtbb
    dpz += quadrupole_integrated_strength * kc * x * x * ckz / 2  # Quadrupole kick
    dpz += sextupole_integrated_strength * kc * x * x * x * ckz / 3  # Sextupole kick

    # ! Time independent
    # dpx = quadrupole_integrated_strength * x  # Quadrupole kick
    # dpx += sextupole_integrated_strength * x * x  # Sextupole kick
    # dpz = 0

    nx = x
    npx = px + dpx
    nz = z
    npz = pz + dpz

    return nx, npx, nz, npz


# One turn map


def single_crab_cavity_interaction_map(
    x: np.float64,
    px: np.float64,
    z: np.float64,
    pz: np.float64,
    integrated_magnet_strengths: typing.List[np.float64] = None,
) -> typing.Tuple[np.float64, np.float64, np.float64, np.float64]:
    nx, npx, nz, npz = general.linear_element(x, px, z, pz, ip_to_cc2)

    if integrated_magnet_strengths is None:
        integrated_magnet_strengths = [
            default_quadrupole_integrated_strength,
            default_sextupole_integrated_strength,
        ]

    # Crab Cavity 2
    nx, npx, nz, npz = crab_cavity(
        nx, npx, nz, npz, betax_cc2, betax_ip, theta, integrated_magnet_strengths
    )
    nx, npx, nz, npz = general.linear_element(nx, npx, nz, npz, ip_to_cc2_inv)
    nx, npx, nz, npz = nonlinear_element(nx, npx, nz, npz)
    nx, npx, nz, npz = general.linear_element(nx, npx, nz, npz, ip_to_cc1)

    # Crab Cavity 1
    nx, npx, nz, npz = crab_cavity(
        nx, npx, nz, npz, betax_cc1, betax_ip, theta, integrated_magnet_strengths
    )
    nx, npx, nz, npz = general.linear_element(nx, npx, nz, npz, ip_to_cc1_inv)

    # One turn map
    nx, npx, nz, npz = general.linear_element(nx, npx, nz, npz, ip_to_ip)
    nz, npz = general.longitudinal_element(
        nz,
        npz,
        energy,
        charge,
        phi_s,
        rf_voltage,
        harmonic_number,
        slip_factor,
        beta_s,
        rf_frequency,
    )

    return nx, npx, nz, npz


def multi_crab_cavity_interaction_map(
    x: np.ndarray,
    px: np.ndarray,
    z: np.ndarray,
    pz: np.ndarray,
    integrated_magnet_strengths: typing.List[np.float64] = None,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    nx = np.zeros_like(x)
    npx = np.zeros_like(x)
    nz = np.zeros_like(x)
    npz = np.zeros_like(x)

    for i, (x_i, px_i, z_i, pz_i) in enumerate(zip(x, px, z, pz)):
        nx_i, npx_i, nz_i, npz_i = single_crab_cavity_interaction_map(
            x_i, px_i, z_i, pz_i, integrated_magnet_strengths
        )
        nx[i] = nx_i.copy()
        npx[i] = npx_i.copy()
        nz[i] = nz_i.copy()
        npz[i] = npz_i.copy()

    return nx, npx, nz, npz


def crab_cavity_interaction_map(
    *x, integrated_magnet_strengths: typing.List[np.float64] = None
):
    if isinstance(x[0], np.ndarray) and len(x[0]) > 1:
        nx, npx, nz, npz = multi_crab_cavity_interaction_map(
            *x, integrated_magnet_strengths
        )

    else:
        nx, npx, nz, npz = single_crab_cavity_interaction_map(
            *x, integrated_magnet_strengths
        )

    return nx, npx, nz, npz
