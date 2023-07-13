import pytest
import numpy as np

from gaussian_fitting.fit_functions.gaussian import fit_gaussian


@pytest.fixture
def x_test():
    return np.arange(0, 100)


@pytest.fixture
def y_test():
    mu, sigma = 0, 0.1
    return np.random.normal(mu, sigma, 100)


def test_gaussian_fitting_basic_call(x_test, y_test):
    fit_params, cov = fit_gaussian(x_test, y_test)
    assert isinstance(fit_params, np.ndarray)
    assert isinstance(cov, np.ndarray)
    assert len(fit_params) == 3
    assert cov.shape == (3, 3)


def test_error_raise_on_array_mismatch():
    x_arr = np.array([0, 1, 2, 3, 4, 5])
    y_arr = np.array([1, 2, 3, 4, 5])
    with pytest.raises(ValueError):
        fit_gaussian(x_arr, y_arr)
