import io
import pathlib
import numpy as np
import typing
from iterative_lattice_analysis.iteration_functions import (
    setup_and_execute_iteration_method,
)

test_dir = pathlib.Path(__file__).parent.absolute()
# sys.path.append(test_dir.parent.absolute().as_posix())


def load_iteration_results(
    directory: pathlib.PurePath,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Load the iteration results from the specified directory"""
    U = np.loadtxt(directory / "U.txt", dtype=np.complex128)
    error = np.loadtxt(directory / "error.txt").astype(np.float64)
    freq = np.loadtxt(directory / "freq.txt").astype(np.float64)
    linear_tunes = np.loadtxt(directory / "linear_tunes.txt").astype(np.float64)

    return freq, error, linear_tunes, U


def has_nan_inf(array: np.ndarray) -> bool:
    """Check if array contains nan or inf"""
    return np.any(np.isnan(array)) or np.any(np.isinf(array))


# * Function to check the data
def check_data(directory: pathlib.PurePath) -> bool:
    test_bool = True
    test_results = io.StringIO()
    working_dir = test_dir  # optimization for python checking local vars first
    test_data_dir = working_dir / "test-data/"

    test_freq, test_error, test_linear_tunes, test_U = load_iteration_results(
        test_data_dir
    )
    freq, error, linear_tunes, U = load_iteration_results(directory)

    if not np.allclose(U, test_U):
        test_results.write("U does not match\n")
        test_bool = False

    if not np.allclose(linear_tunes, test_linear_tunes):
        test_results.write("Linear tunes do not match\n")
        test_bool = False

    for i in range(len(test_freq)):
        if not has_nan_inf(freq[i]) and not has_nan_inf(test_freq[i]):
            if not np.allclose(freq[i], test_freq[i]):
                test_results.write(
                    f"Frequency {i}: {freq[i]} != {test_freq[i]} ({np.linalg.norm(np.abs(freq[i] - test_freq[i])):2e})\n"
                )
                test_bool = False

        if not has_nan_inf(error[i]) and not has_nan_inf(test_error[i]):
            if not np.allclose(error[i], test_error[i]):
                test_results.write(
                    f"Error {i}: {error[i]} != {test_error[i]} ({np.linalg.norm(np.abs(error[i] - test_error[i])):2e})\n"
                )
                test_bool = False

    if test_bool:
        test_results.write("All tests passed\n")

    with open(working_dir / "test_results.txt", "w") as f:
        f.write(test_results.getvalue())

    return test_bool


if __name__ == "__main__":
    max_cores = 4  # Number of cores to use
    dim = 2  # Spatial dimention of problem
    order = 3  # Order of square matrix method
    res = None  # Tune resonance

    ntheta = int(2**4)  # Number of points to sample for alpha and beta
    numiters = int(20)  # Number of iterations to perform for iteration method

    number_x_samples = 10
    number_y_samples = 15

    # Initial Positions
    x_range = (-0.035, 0.030)
    y_range = (0, 0.013)

    results_folder = test_dir / "iteration-results/"
    madx_folder = test_dir / "test-tpsa/"

    setup_and_execute_iteration_method(
        dim=dim,
        order=order,
        res=res,
        x_range=x_range,
        y_range=y_range,
        number_position_samples=(number_x_samples, number_y_samples),
        number_angle_samples=ntheta,
        number_iterations=numiters,
        function=madx_folder,
        cores=max_cores,
        newton_inverse=False,
    )

    if check_data(results_folder):
        print("All Tests Passed!")
    else:
        print("Tests Failed! See test_results.txt for more information.")
