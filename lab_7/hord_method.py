import matplotlib.pyplot as plt
import numpy as np

from equations import fun_with_param, fun, derivative_phi


def hord_method_with_params(x0, iterations, a, b, c, d, eps, round_to):
    x = x0
    x_prev = x0 + 2 * eps
    i = 0

    while np.abs(x - x_prev) >= eps and i < iterations:
        # if np.abs(derivative_phi_with_param(a, b, c, x)) >= 1:
        #     return print("Итерационный процесс расходится")
        x = x - fun_with_param(a, b, c, d, x) / (fun_with_param(a, b, c, d, x) - fun_with_param(a, b, c, d, x_prev)) * (
                x - x_prev)
        x_prev = x
        i += 1

    print("Число итераций: ", i)
    print("X: ", round(x, round_to))
    y = fun_with_param(a, b, c, d, x)
    plt.scatter(x, y, color="red")


def hord_method_without_params(x0, iterations, eps, round_to):
    x = x0
    x_prev = x0 + 2 * eps
    i = 0

    while np.abs(x - x_prev) >= eps and i < iterations:
        if np.abs(derivative_phi(x)) >= 1:
            return print("Итерационный процесс расходится")
        x = x - fun(x) / (fun(x) - fun(x_prev)) * (x - x_prev)
        x_prev = x
        i += 1

    print("Число итераций: ", i)
    print("Без параметров: ", round(x, round_to))
