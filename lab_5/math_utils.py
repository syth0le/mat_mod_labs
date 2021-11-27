import random

import numpy as np

from config import Config


def generate_random_variables(size):
    r = []
    for i in range(size):
        r.append(random.random())
    return r


def get_function_max(linspaceLen):
    a, b, func = Config.MIN, Config.MAX, Config.our_function
    func_values = []
    for x in np.linspace(a, b, linspaceLen):
        func_values.append(func(x))

    return np.abs(max(func_values) - min(func_values)), min(func_values)
