from equations import *
import matplotlib.pyplot as plt


def newton_method_with_param(x, n, a, b, c, d, eps, number):
    root = x
    # число итерций
    N = 0
    for i in range(n):
        N += 1
        # if abs(derivative_phi_with_param(a, b, root)) >= 1:
        #     return print("Итерационный процесс расходится")
        root = x - (fun_with_param(a, b, c, d, x) / derivative_fun_with_param(a, b, c, x))
        # Если разница между текущим корнем и предыдущим меньше eps
        if abs(root - x) < eps:
            break
        x = root
    print("Число итераций: ", N)
    print("С параметрами: ", round(root, number))
    plt.scatter(root, 0)


def newton_method_without_param(x, n, eps, number):
    root = x
    # число итерций
    N = 0
    for i in range(n):
        N += 1
        # if abs(derivative_phi(x)) >= 1:
        #     return print("Итерационный процесс расходится")
        root = x - (fun(x) / derivative_fun(x))
        # Если разница между текущим корнем и предыдущим меньше eps
        if abs(root - x) < eps:
            break
        x = root
    print("Число итераций: ", N)
    print("Без параметров: ", round(root, number))
    plt.scatter(root, 0)
