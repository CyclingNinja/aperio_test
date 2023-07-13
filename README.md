# Fitting Routines for noisy data

## Installation
Package may be installed in the standard way via the command line
`python -m pip install  .`

Installation via the `setup.cfg` file, so please also see here for dependencies.

## Tests
The tests are written using the pytest framework and deps may be installed using
`python -m pip install '.[tests]'`
Once the package is installed tests may be run from the command line with
`pytest tests`


## Usage
Individual routines are imported from the fit functions module. Please see docstrings for details on individal functions.

### Example


```python
from gaussian_fitting.fit_functions.gaussian import fit_gaussian

# generate some sample data
x_arr = np.arange(0, 100)
y_arr = np.random.normal(0, 0.1, 100)

fit_params, cov = fit_gaussian(x_test, y_test)
```