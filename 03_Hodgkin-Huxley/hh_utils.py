import numpy as np

__all__ = ['vtrap','coeffs']

# this avoids problems when the rate function is 0/0
def vtrap(x,y):
    if np.isscalar(x):
        return y*(1-x/y/2) if abs(x/y)<1e-6 else x/(np.exp(x/y) - 1)
    z = np.zeros_like(x, dtype=float)
    idx = abs(x/y) < 1e-6
    z[idx] = y*(1-x[idx]/y/2)
    np.logical_not(idx, out=idx)
    z[idx] = x[idx]/(np.exp(x[idx]/y) - 1)
    return z

# returns x_ss and tau_x
def coeffs(v, alpha_fun, beta_fun):
    a,b = alpha_fun(v),beta_fun(v)
    return a/(a+b), 1/(a+b)
