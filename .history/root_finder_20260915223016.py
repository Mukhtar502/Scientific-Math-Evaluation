import numpy as np
from scipy.optimize import fsolve

def evaluate_model_performance(func, initial_guess):
    root = fsolve(func, initial_guess)
    is_valid = np.isclose(func(root), 0.0)
    return root[0], is_valid

def my_function(x):
    return x**2 - 4