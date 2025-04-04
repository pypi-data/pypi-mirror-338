import typing
import pathlib
import logging
import numpy as np
import sympy as sp
from PyTPSA.tpsa import tpsa
from PyTPSA.tpsa import sin as sin_tpsa
from PyTPSA.tpsa import cos as cos_tpsa
from PyTPSA.tpsa import tan as tan_tpsa
from sqrmat_method.sqrmat import tpsvar
from sqrmat_method.sqrmat_method import square_matrix
from madx_ptc_utils.python_from_ptc import python_from_ptc


# Copies of functions from personal python library to avoid dependency
def __newton_inv_2d__(
    func: typing.Callable,
    invfunc: typing.Callable,
    funcjac: typing.Callable,
    w: np.ndarray,
    iterations: int = 10,
    max_trials: int = 10,
    tol: float = 1e-4,
) -> tuple:
    """
    Starting from a guess z, finds the inverse of func such that func(z)=w using Newton's method

    Input
    _____
        func: 4D Transformation from the z space into the w space; [wx, wxc, wy, wyc] = func([zx, zxc, zy, zyc])
        invfunc: 4D Transformation from the w space into the z space; [zx, zxc, zy, zyc] = func([wx, wxc, wy, wyc])
        funcjac: 4,4 Jacobian of func
        w: Numpy Array of points to invert (numbers of points, 4)

    Returns
    _______
        zxsol, zxcsol, zysol, zycsol: Arrays of the numerical inverse of the points from w in the form z_x, z*_x, z_y, z*_y
    """

    # ! Use this version

    random_amplitude = 0.2
    zsol = []

    for ws in w:
        trz = invfunc(ws)

        for _ in range(iterations):
            jac = funcjac(trz)
            trial = 0
            while np.linalg.det(jac) < tol and trial < max_trials:
                # print(xini, "warning, small jac, adjusting the seed")
                xrand = np.random.randn() * random_amplitude
                yrand = np.random.randn() * random_amplitude
                trz += np.array([xrand, xrand, yrand, yrand])
                jac = funcjac(trz)
                trial += 1

            # This may look redundant but it is not, for some reason this is the fastest
            new_z = -np.linalg.solve(jac, np.array(func(trz) - ws)) + trz
            trz = new_z.tolist()

        zsol.append(trz)

    return np.array(zsol, dtype=w.dtype)


def __jacobian_lamdify__(
    forward_function: typing.Callable, dim: int, input_: str = "single"
) -> typing.Callable:
    """
    Takes in a function and returns a function that returns the jacobian of the function

    Input
    _____
        forward_function: function that takes in dim variables and returns dim variables one
            iteration later.
        dim: number of variables in the function
        input_: string that is either "single" or "multiple" and determines the input type of the function

    Output
    ______
        jac: function that takes in dim variables and returns the jacobian of the function
    """

    variables_ = sp.symbols(", ".join([f"x_{i}" for i in range(dim)]))

    if input_ == "single":
        forward_variables = forward_function(variables_)
    elif input_ == "multiple":
        forward_variables = forward_function(*variables_)
    else:
        raise ValueError("input must be either 'single' or 'multiple'")

    jac = sp.Matrix(forward_variables).jacobian(variables_)
    jac_func = sp.lambdify(variables_, jac, modules="numpy")

    if input_ == "multiple":
        return_func = jac_func

    elif input_ == "single":

        def jac_single(args):
            return jac_func(*args)

        return_func = jac_single

    return return_func


def check_for_imag(
    x: np.ndarray, atol: float = 1e-8, return_real: bool = True, warn: bool = False
) -> np.ndarray:
    """Removes small imaginary numbers.

    Inputs:
        x: np.ndarray
            Array of complex numbers

        atol: float
            Tolerance for small imaginary part

    Returns:
        r: np.ndarray
            Array of the real part of x. If the imaginary parts are large, x is returned.
    """

    imag_x = np.imag(x)
    zero_imag = np.all(np.isclose(imag_x, 0, atol=atol))

    if warn and not zero_imag and not np.any(np.isnan(imag_x)):
        # Avoids printing the warning if the reason for non zero imaginary
        # component is the value is nan, which is a commom issue
        logging.warning("Some components of X are not real.")

    if return_real or zero_imag:
        return np.real(x)

    return x


def sympy_tpsa_numpy_trig(arg, trig_functions: typing.List[str]) -> typing.List:
    """
    Apply specified trigonometric functions to the input argument.

    This function applies the trigonometric functions specified in the
    `trig_functions` list to the input `arg`. If `arg` is an instance of
    sympy.Basic, sympy's trigonometric functions are used. Otherwise, if `arg`
    is an instance of tpsa, the corresponding tpsa trigonometric functions are
    used. If `arg` is neither, the real part of the result is returned.

    Parameters
    ----------
    arg : sympy.Basic, tpsa, or other
        The argument to apply the trigonometric functions to.
    trig_functions : list of str
        The list of trigonometric functions to apply. Valid functions are
        'sin', 'cos', and 'tan'.

    Returns
    -------
    list
        A list of the results of applying the specified trigonometric functions
        to `arg`.

    Raises
    ------
    Exception
        If no valid trigonometric functions were selected.

    """
    valid_trig_functions = ["sin", "cos", "tan"]

    return_list = []

    if isinstance(arg, sp.Basic):
        if "sin" in trig_functions:
            return_list.append(sp.sin(arg))
        if "cos" in trig_functions:
            return_list.append(sp.cos(arg))
        if "tan" in trig_functions:
            return_list.append(sp.tan(arg))

    else:
        if "sin" in trig_functions:
            return_list.append(sin_tpsa(arg))
        if "cos" in trig_functions:
            return_list.append(cos_tpsa(arg))
        if "tan" in trig_functions:
            return_list.append(tan_tpsa(arg))

    if not isinstance(arg, tpsa) and not isinstance(arg, sp.Basic):
        return_list = np.real(return_list).tolist()

    if return_list:
        return return_list

    else:
        raise Exception(
            "No valid trig functions were selected. Must select at least one of {valid_trig_functions}"
        )


def linear_tunes_and_unitary_transformation(
    M: np.ndarray, unitary: bool = False
) -> typing.Tuple[np.ndarray, np.ndarray]:
    eig, U = np.linalg.eig(M)

    tunes = np.arctan2(eig[0::2].imag, eig[0::2].real) / 2 / np.pi

    if unitary:
        u, _, v = np.linalg.svd(U)
        U = u @ v

    return tunes, U


def get_transformation(M: np.ndarray, unitary: bool = False) -> typing.Tuple:
    eig, U = np.linalg.eig(M)

    tunes = np.arctan2(eig[0::2].imag, eig[0::2].real) / 2 / np.pi

    if unitary:
        u, _, v = np.linalg.svd(U)
        U = u @ v

    return tunes, U


def get_linear_row(xmap: typing.Callable, dim: int):
    number_of_elements = 2 * dim
    c = np.empty(number_of_elements, dtype=np.complex128)

    for i in range(number_of_elements):
        c[i] = xmap.element(i + 1)

    return c


def get_linear_map_and_unitary_transformation(
    xmap: typing.Callable, dim: int, unitary: bool = False
) -> typing.Tuple[np.ndarray, np.ndarray]:
    linear_map = np.eye(2 * dim, dtype=np.complex128)

    for i, xi in enumerate(xmap):
        linear_map[i, :] = get_linear_row(xi, dim)

    linear_tunes, U = linear_tunes_and_unitary_transformation(linear_map, unitary)

    return linear_tunes, U


def get_iteration_objects(
    dim: int,
    order: int,
    res: typing.Tuple[int, int],
    function: typing.Union[typing.Callable, pathlib.PosixPath],
    newton_inverse: bool = False,
    test: bool = False,
) -> typing.Tuple[
    np.ndarray, np.ndarray, typing.Callable, typing.Callable, typing.Callable
]:
    if isinstance(function, pathlib.PosixPath):
        madx_func = python_from_ptc(function)
    else:
        madx_func = function

    if order != 0:
        use_sqrmat = True
    else:
        use_sqrmat = False
        order = 3  # * dumby value
        if newton_inverse:
            logging.warning(
                (
                    "Newton's method inverse is True, but the Square Matrix Method is not"
                    "being used. Parameter is being ignored."
                )
            )

    sqrmat = square_matrix(dim, order)
    xtps = tpsvar(dim, order)
    xmap = madx_func(*xtps.vars)
    linear_tunes, U = get_linear_map_and_unitary_transformation(xmap, dim)
    Uinv = np.linalg.inv(U)
    xofz = U.dot(sqrmat.variables).tolist()  # X in terms of Z
    # Linear action angle variables
    zmap = Uinv.dot(
        [xi.composite(xofz) for xi in xmap]  # X' in terms of Z
    ).tolist()  # Z' in terms of Z

    if use_sqrmat:
        sqrmat.construct_square_matrix(periodic_map=zmap)
        sqrmat.get_transformation(res=res)

        # ERROR CHECK
        if test:
            sqrmat_pass, sqrmat_num_errors, sqrmat_max_error = sqrmat.test_sqrmat()

            if not sqrmat_pass:
                logging.warning(
                    (
                        "Square Matrix did not pass test! Number of Errors:"
                        f"{sqrmat_num_errors}, Max Error: {sqrmat_max_error}."
                    )
                )

        if newton_inverse:
            jac = __jacobian_lamdify__(sqrmat.w, 2 * dim, input_="single")

            def inverse_function(w: np.ndarray) -> np.ndarray:
                z = __newton_inv_2d__(sqrmat.w, sqrmat.z, jac, w.T).T
                return z

            return_tuple = linear_tunes, U, sqrmat.w, inverse_function, madx_func

        else:
            return_tuple = linear_tunes, U, sqrmat.w, sqrmat.z, madx_func

    else:

        def identity(x):
            return x

        return_tuple = linear_tunes, U, identity, identity, madx_func

    return return_tuple


def create_grid(
    spacial_dim_ranges: typing.Tuple[typing.Tuple[float, float]],
    number_of_samples: typing.Tuple[int],
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # Creating arrays of intial points
    iniarrs = [
        np.linspace(*range_, num=number)
        for range_, number in zip(spacial_dim_ranges, number_of_samples)
    ]

    iniarrs = np.meshgrid(*iniarrs)
    iniarrs = tuple(xini.flatten() for xini in iniarrs)

    return iniarrs


def data_prep(
    dim: int,
    order: int,
    res: list,
    iniarrs: typing.Tuple[np.ndarray, np.ndarray, np.ndarray],
    function: typing.Union[
        typing.Callable[
            [np.float64, np.float64, np.float64, np.float64, np.float64, np.float64],
            typing.Tuple[
                np.float64, np.float64, np.float64, np.float64, np.float64, np.float64
            ],
        ],
        pathlib.PosixPath,
    ],
    ignore_constants: bool = False,
    newton_inverse: bool = False,
) -> typing.Tuple[
    typing.List[np.ndarray],
    np.ndarray,
    np.ndarray,
    typing.Callable,
    typing.Callable,
    typing.Callable,
]:
    # Initial Momentum
    pi = [0] * dim

    (
        linear_tunes,
        U,
        wfunc,
        winvfunc,
        madx_func,
    ) = get_iteration_objects(dim, order, res, function, newton_inverse, test=True)
    Uinv = np.linalg.inv(U)

    iteration_method_arguments = []

    for vars_i_generator in zip(*iniarrs):
        vars_i = list(vars_i_generator)
        xi = []

        for i in range(dim):
            xi.append(vars_i[i])
            xi.append(pi[i])

        zi = Uinv.dot(xi)
        wi = wfunc(zi)
        iteration_method_arguments.append(wi[::2])

    return iteration_method_arguments, linear_tunes, U, wfunc, winvfunc, madx_func


def get_dynamic_apecture(
    error_results: np.typing.ArrayLike,
    dynaimc_aperture_scale: int,
    log_threshold: float = -8,
    log_offset: float = 1e-16,
):
    dynamic_aperture = (
        np.sum(
            (
                np.log10(error_results[~np.isnan(error_results)] + log_offset)
                < log_threshold
            )
        )
        / dynaimc_aperture_scale
    )

    return dynamic_aperture
