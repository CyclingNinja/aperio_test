import numpy as np
from scipy.optimize import curve_fit


def fit_gaussian(x_arr, y_arr, **kwargs):
    """
    Function taking an x domain and a y varible and attempts to fit a gaussian to it.
    Returns a tuple of the fit parameters and the covarience

    Parameters
    ----------
    x_arr: arraylike
        Independant variable, array consistent of floats
    y_arr: arraylike
        Dependant varialbe, array consistent of floats
    kwargs: dict
        Dictonary to pass extra arguments to scipy.optimize.curve_fit
        e.g. a p0 list or sigma value

    Returns
    -------
    optimal_params: ndarray
        Array defining parameters so the sum or square residuals is minimised
    covariance: ndarray
        2-D array, see scipy.optimize.curve_fit for full details
    """
    def gaussian(x, a, x0, sigma):
        return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

    if len(x_arr) == len(y_arr):
        fitted_data = curve_fit(f=gaussian,
                              xdata=x_arr,
                              ydata=y_arr,
                              p0=None,
                              *kwargs)
    else:
        raise ValueError('X and Y array dimensions do not match')
    return fitted_data[0], fitted_data[1]
