import matplotlib.pyplot as plt

from equations import *


def iteration_method_with_param(x0, eps, number, a, b, c, d):
    # if abs(derivative_phi_with_param(a, b, c, x)) >= 1:
    #     print(abs(derivative_phi_with_param(a, b, c, x)))
    #     return print("Итерационный процесс расходится")

    root = phi_with_param(a, b, c, d, x0)
    # print('first:', root)
    x = x0
    n = 0
    for i in range(50):
        x = root
        root = phi_with_param(a, b, c, d, x)
        n += 1
        if abs(x - root) < eps:
            break
    # while abs(root - x) >= eps:
    #     # if abs(derivative_phi_with_param(a, b, c, root)) >= 1:
    #     #     print('@@@@', abs(derivative_phi_with_param(a, b, c, root)))
    #     #     return print("Итерационный процесс расходится")
    #     n += 1
    #     x = root
    #     # breakpoint()
    #     root = phi_with_param(a, b, c, d, x)
    print("Число итераций: ", n)
    print("X: ", round(root, number))
    y = fun_with_param(a, b, c, d, root)
    plt.scatter(root, y, color="red")


def iteration_method_without_param(x, eps, number):
    # if abs(derivative_phi(x)) >= 1:
    #     return print("Итерационный процесс расходится")
    root = phi(x)
    n = 0
    while abs(root - x) >= eps:
        # if abs(derivative_phi(root)) >= 1:
        #     return print("Итерационный процесс расходится")
        n += 1
        x = root
        root = phi(x)
    print("Число итераций: ", n)
    print("Без параметров: ", round(root, number))
