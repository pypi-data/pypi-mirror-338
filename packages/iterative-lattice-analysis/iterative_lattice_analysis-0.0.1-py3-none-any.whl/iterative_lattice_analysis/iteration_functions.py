import typing
import pathlib
import warnings
import multiprocessing
import functools
import time
import io
import numpy as np
import copy
import dill
from . import support_functions

# TODO - Add type hints to functions
# TODO - Add docstrings to functions
# TODO - Convert madx_func and one_turn_map (of iteration_method_script) to take
# TODO      arguments of the shape (samples, features)


# * Classes
class IterationMethodError(Exception):
    """
    Raised when a nan is encountered in the iteration method.

    Created so that it can be ignored and the iteration method can continue as designed
    while other errors can still be caught and raised.
    """

    pass


# * Functions
def iteration_step(
    dtheta: np.ndarray,
    theta0: np.ndarray,
    freq: typing.List[float],
    one_turn_map: typing.Callable[[np.ndarray], np.ndarray],
) -> typing.Tuple[np.ndarray, typing.List[float]]:

    warnings.warn(
        "iteration_step is deprecated, use generalized_iteration_step instead",
        DeprecationWarning,
    )

    n1, n2 = theta0[0].shape  # number of sample points
    t = theta0 + dtheta

    wx = np.exp(1j * t[0])
    wxc = np.conj(wx)
    wy = np.exp(1j * t[1])
    wyc = np.conj(wy)

    nwx, _, nwy, _ = one_turn_map(np.array([wx, wxc, wy, wyc]))

    phix = -1j * np.log(nwx / wx) - freq[0]
    phiy = -1j * np.log(nwy / wy) - freq[1]

    phix_fft = np.fft.fft2(phix)
    phiy_fft = np.fft.fft2(phiy)

    fl1 = np.fft.fftfreq(n1, 1 / n1)

    if n1 == n2:
        fl2 = fl1
    else:
        fl2 = np.fft.fftfreq(n2, 1 / n2)

    freq1list, freq2list = np.meshgrid(fl1, fl2, indexing="ij")
    freq1list[0, 0] = 1.0
    freq2list[0, 0] = 1.0

    newfreq = [
        (freq[0] + phix_fft[0, 0] / n1 / n2).real,
        (freq[1] + phiy_fft[0, 0] / n1 / n2).real,
    ]

    res_term = np.exp(1j * freq1list * newfreq[0] + 1j * freq2list * newfreq[1]) - 1

    theta_mx = phix_fft / res_term
    theta_my = phiy_fft / res_term
    theta_mx[0, 0] = 0.0j
    theta_my[0, 0] = 0.0j

    dt = np.zeros_like(dtheta)
    dt[0] = np.fft.ifft2(theta_mx)
    dt[1] = np.fft.ifft2(theta_my)

    return dt, newfreq


def iteration_method(
    wxini: float,
    wyini: float,
    mux: float,
    muy: float,
    numiters: int,
    nsample: int,
    one_turn_map: typing.Callable[[np.ndarray], np.ndarray],
    return_tracking: bool = False,
) -> typing.Union[
    typing.Tuple[typing.List[float], np.ndarray],
    typing.Tuple[typing.List[float], np.ndarray, np.ndarray],
]:

    warnings.warn(
        "iteration_method is deprecated, use generalized_iteration_method instead",
        DeprecationWarning,
    )

    dim = 2
    nalpha = nsample
    nbeta = nsample

    errors = []

    alphas = np.linspace(0, 2 * np.pi, num=nalpha, endpoint=False)
    betas = np.linspace(0, 2 * np.pi, num=nbeta, endpoint=False)
    aa, bb = np.meshgrid(alphas, betas, indexing="ij")

    theta1ini = -1j * np.log(wxini)
    theta2ini = -1j * np.log(wyini)
    thetas = np.zeros((dim, nalpha, nbeta), dtype=np.complex128)
    thetas[0] = aa + theta1ini
    thetas[1] = bb + theta2ini

    dt = np.zeros_like(thetas)

    freqs = [mux, muy]

    try:
        for _ in range(numiters):
            thetas_old = np.copy(thetas)

            dt, freqs = iteration_step(dt, thetas, freqs, one_turn_map)

            if np.any(np.isnan(dt)) or np.any(np.isinf(dt)) or np.any(np.isnan(freqs)):
                raise IterationMethodError("NaN encountered in iteration method")

            thetas[0] = aa + theta1ini - dt[0, 0, 0]
            thetas[1] = bb + theta2ini - dt[1, 0, 0]

            # Error is ||W_n - W_(n-1)|| normalized by number of sample points
            errors.append(
                np.linalg.norm(
                    ((np.exp(1j * thetas) - np.exp(1j * thetas_old)).flatten())
                )
                / thetas.size
            )

    except IterationMethodError as e:
        # A nan was encountered in the iteration method
        # logging.error(e)
        freqs = np.full(dim, np.nan)
        errors = np.full(numiters, np.nan)
        thetas = np.full((dim, nalpha, nbeta), np.nan)

    except Exception as e:
        # Some other error occurred
        raise e

    if return_tracking:
        return freqs, thetas, errors

    return freqs, errors


def generalized_iteration_step(
    dtheta: np.ndarray,
    theta0: np.ndarray,
    freq: np.ndarray,
    one_turn_map: typing.Callable[[np.ndarray], np.ndarray],
) -> typing.Tuple[np.ndarray, np.ndarray]:
    """
    Perform a single step of the iteration method.

    Parameters
    ----------
    dtheta : np.ndarray
        Incremental change in theta values.
    theta0 : np.ndarray
        Initial theta values.
    freq : np.ndarray
        Frequency values.
    one_turn_map : callable
        Function that maps the input array to the next iteration or "turn".

    Returns
    -------
    dt : np.ndarray
        Updated incremental change in theta values.
    newfreq : np.ndarray
        Updated frequency values.
    """
    num_samples = theta0[0].shape  # number of sample points
    t = theta0 + dtheta

    # For broadcasting
    freq_slice = (slice(None), *([np.newaxis] * len(num_samples)))
    fft_slice = (slice(None), *([0] * len(num_samples)))
    fft_axes = tuple(range(1, len(num_samples) + 1))

    w = np.exp(1j * t)
    wc = w.conj()
    warg = np.zeros((2 * w.shape[0], *num_samples), dtype=w.dtype)
    warg[::2] = w
    warg[1::2] = wc

    nw = one_turn_map(warg)

    phi = -1j * np.log(nw[::2] / w) - freq[freq_slice]

    phi_fft = np.fft.fftn(phi, axes=fft_axes)

    freqlist = np.array(
        np.meshgrid(*[np.fft.fftfreq(n, 1 / n) for n in num_samples], indexing="ij")
    )
    freqlist[fft_slice] = 1.0

    newfreq = (freq + phi_fft[fft_slice] / np.prod(num_samples)).real

    res_term = np.exp(1j * np.sum(freqlist * newfreq[freq_slice], axis=0)) - 1

    theta_m = phi_fft / res_term
    theta_m[fft_slice] = 0.0j

    dt = np.fft.ifftn(theta_m, axes=fft_axes)

    return dt, newfreq


def generalized_iteration_method(
    wini: np.ndarray,
    freqs: np.ndarray,
    numiters: int,
    nsample: typing.List[int],
    one_turn_map: typing.Callable[[np.ndarray], np.ndarray],
    return_tracking: bool = False,
) -> typing.Union[
    typing.Tuple[np.ndarray, np.ndarray],
    typing.Tuple[np.ndarray, np.ndarray, np.ndarray],
]:
    """
    Use the iterative method to compute the frequencies and diffeomorphism to a pure
    rotation at the given coordinate.

    Parameters
    ----------
    wini : np.ndarray
        Initial point to begin calculations around.
    freqs : np.ndarray
        Initial frequency values.
    numiters : int
        Number of iterations to perform.
    nsample : list of int
        List of sample sizes for each dimension.
    one_turn_map : callable
        Function that maps the input array to the next iteration or "turn" of the
        lattice.
    return_tracking : bool, optional
        If True, return the tracking data. Defaults to False.

    Returns
    -------
    freqs : np.ndarray
        Computed frequency values.
    errors : np.ndarray
        Computed error values for each iteration.
    thetas : np.ndarray, optional
        Computed theta values for each iteration. Only returned if `return_tracking` is True.

    Raises
    ------
    IterationMethodError
        If a NaN is encountered in the iteration method.
    """
    dim = len(wini)
    errors = []

    # For broadcasting
    theta_slice = (slice(None), *([np.newaxis] * dim))
    dt_slice = (slice(None), *([0] * dim))

    dimorphism_points = np.array(
        np.meshgrid(
            *[np.linspace(0, 2 * np.pi, num=n, endpoint=False) for n in nsample],
            indexing="ij",
        )
    )

    thetaini = -1j * np.log(wini)

    thetas = np.zeros((dim, *nsample), dtype=np.complex128)

    thetas = dimorphism_points + thetaini[theta_slice]

    dt = np.zeros_like(thetas)

    try:
        for _ in range(numiters):
            thetas_old = np.copy(thetas)

            dt, freqs = generalized_iteration_step(dt, thetas, freqs, one_turn_map)

            if np.any(np.isnan(dt)) or np.any(np.isinf(dt)) or np.any(np.isnan(freqs)):
                raise IterationMethodError("NaN encountered in iteration method")

            thetas = (
                dimorphism_points + thetaini[theta_slice] - dt[dt_slice][theta_slice]
            )

            # Error is ||W_n - W_(n-1)|| normalized by number of sample points
            errors.append(
                np.linalg.norm(
                    ((np.exp(1j * thetas) - np.exp(1j * thetas_old)).flatten())
                )
                / thetas.size
            )

    except IterationMethodError as e:
        # A nan was encountered in the iteration method
        # logging.error(e)
        freqs = np.full(dim, np.nan)
        errors = np.full(numiters, np.nan)
        thetas = np.full((dim, *nsample), np.nan)

    except Exception as e:
        # Some other error occurred
        raise e

    if return_tracking:
        return freqs, thetas, errors

    return freqs, errors


def __one_turn_map__(ws: np.ndarray) -> np.ndarray:
    """
    Map the input array to the next iteration or "turn" of the lattice.

    !!!! WARNING !!!
    This is meant to be used only within the iteration method and not on its own.

    Functions inside are global from the setup_and_execute_iteration_method function in
    order to allow for pickling and multiprocessing.
    """
    dim, nalpha, nbeta = ws.shape
    w = ws.reshape(dim, -1)
    w = winvfunc(w)
    w = U.dot(w)
    w = support_functions.check_for_imag(w)
    w = madx_func(*w)
    w = Uinv.dot(w)
    w = wfunc(w)
    return w.reshape(dim, nalpha, nbeta)


def setup_and_execute_iteration_method(
    dim: int,
    order: int,
    res: list,
    x_range: tuple,
    y_range: tuple,
    number_position_samples: tuple,
    number_angle_samples: int,
    number_iterations: int,
    function: typing.Union[pathlib.PosixPath, typing.Callable],
    ignore_constants: bool = False,
    newton_inverse: bool = False,
    cores: int = 1,
    results_folder: pathlib.PosixPath = None,
) -> None:
    """Main function to perform the iteration method.

    Parameters
    ----------
    dim : int
        Number of spacial dimensions.
    order : int
        The order of the problem.
    res : list
        Resonances to be resolved.
    x_range : tuple
        The range of x values to be sampled.
    y_range : tuple
        The range of y values to be sampled.
    number_position_samples : tuple
        The number of position samples in x and y.
    number_angle_samples : int
        The number of angle samples.
    number_iterations : int
        The number of iterations to perform.
    function : Union[pathlib.PosixPath, Callable]
        The path to the MADX PTC folder or a callable function.
    ignore_constants : bool, optional
        Whether to ignore constants in the MADX PTC folder. Defaults to False.
    newton_inverse : bool, optional
        Whether to use the Newton inverse for the square matrix method. Defaults to
        False.
    cores : int, optional
        The number of cores to use for multiprocessing. Defaults to 1.
    results_folder : pathlib.PosixPath, optional
        The folder to save the results in. Defaults to None which saves the results in
        the current directory under "iteration-results".

    Raises
    ------
    Exception
        If the output folder exists and is not a directory.

    Returns
    -------
    None
    """
    global U, Uinv, wfunc, winvfunc, madx_func

    if results_folder is None:
        results_folder = pathlib.Path("./iteration-results/")

    if results_folder.exists() and not results_folder.is_dir():
        raise Exception("Output folder exists and is not a directory")

    # * Data Prep
    number_x_samples, number_y_samples = number_position_samples

    print(f"{number_x_samples*number_y_samples} sample points")
    print("Preparing Data...")

    xiniarr, yiniarr = support_functions.create_grid(
        (x_range, y_range), (number_x_samples, number_y_samples)
    )

    (
        iteration_method_arguments,
        linear_tunes,
        U,
        wfunc,
        winvfunc,
        madx_func,
    ) = support_functions.data_prep(
        dim, order, res, (xiniarr, yiniarr), function, newton_inverse
    )

    Uinv = np.linalg.inv(U)

    partial_iteration_method = functools.partial(
        generalized_iteration_method,
        freqs=2 * np.pi * linear_tunes,
        numiters=number_iterations,
        nsample=[number_angle_samples] * dim,
        one_turn_map=__one_turn_map__,
    )

    # * Run Iteration Method

    print("Running Iteration Method...")

    start = time.perf_counter()

    if cores == 1:
        results = [partial_iteration_method(ai) for ai in iteration_method_arguments]

    else:
        with multiprocessing.Pool(cores) as pool:
            results = pool.map(partial_iteration_method, iteration_method_arguments)

    iter_time = time.perf_counter() - start

    print(f"Iteration Done: {iter_time} (s)")

    # * Saving Results
    freq_results = []
    error_results = []

    for fi, ei in results:
        freq_results.append(fi)
        error_results.append(min(ei))

    freq_results = np.array(freq_results)
    error_results = np.array(error_results)

    if not results_folder.exists():
        results_folder.mkdir()

    np.savetxt(results_folder / "U.txt", U)
    np.savetxt(results_folder / "linear_tunes.txt", linear_tunes)
    np.savetxt(results_folder / "xini.txt", xiniarr)
    np.savetxt(results_folder / "yini.txt", yiniarr)
    np.savetxt(results_folder / "freq.txt", freq_results)
    np.savetxt(results_folder / "error.txt", error_results)

    # Writing runtime info to file
    runtime_info = io.StringIO()

    runtime_info.write(time.strftime("%Y-%m-%d %H:%M"))
    runtime_info.write("\n")
    runtime_info.write(f"Number of Cores: {cores}\n")
    runtime_info.write(f"Total Time: {iter_time} s\n")
    runtime_info.write(f"Square Matrix Order: {order}\n")
    runtime_info.write(f"Number of Points: {len(xiniarr)}\n")
    runtime_info.write(f"Number of Angle Sample Points: {number_angle_samples**2}\n")
    runtime_info.write(f"X Range: {np.min(xiniarr)}, {np.max(xiniarr)}\n")
    runtime_info.write(f"Y Range: {np.min(yiniarr)}, {np.max(yiniarr)}\n")

    with open(results_folder / "runtime-info.txt", "w") as text_file:
        text_file.write(runtime_info.getvalue())

    print("Done!")

    return
