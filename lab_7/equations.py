import numpy as np


# Фунция с параметрами
def fun_with_param(a, b, c, d, x):
    return a * (x**3) + b * (x**2) + c * x + d


def phi_with_param(a, b, c, d, x):
    return a * (x**3) + b * (x**2) + (c + 1) * x + d


def derivative_fun_with_param(a, b, c, x):
    return 3 * a * (x**2) + 2 * b * x + c


def derivative_phi_with_param(a, b, c, x):
    return 3 * a * (x**2) + 2 * b * x + c + 1


# Функция без параметров
def fun(x):
    return x * (2 ** x) - 1


def phi(x):
    return 2 ** (-x)


def derivative_fun(x):
    return (2 ** x) * (1 + np.log(2) * x)


def derivative_phi(x):
    return -1 * np.log(2) / (2 ** x)
