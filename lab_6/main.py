from typing import Callable

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


func = lambda x: x ** 2 + 2 * np.exp(x)
# так как у функция возврастающая на положительных иксах и убывающая на отрицательных
# проще найти минимумы


def drawGraphic(a, b, func):
    x = np.linspace(a, b, 10000)
    sns.set_theme(style="darkgrid")
    sns.lineplot(x, func(x))
    plt.show()


def golden_section(a: int, b: int, eps: float, func: Callable):
    fi = 0.5 * (1 + np.sqrt(5))  # пропорция золотого сечения
    x1 = b - (b - a) / fi
    x2 = a + (b - a) / fi
    y1 = func(x1)
    y2 = func(x2)
    x = 0
    while np.abs(b - a) < eps:
        if y1 > y2:
            a = x1
        else:
            b = x2

    return (a + b) / 2


def fibonacci_method(a: int, b: int, n: int, func: Callable):
    # x1 = a + (b - a) * Fn-2 / Fn
    # x2 = a + (b - a) * Fn-1 / Fn
    # y1 = func(x1)
    # y2 = func(x2)
    while n > 1:
        n -= 1
        if y1 > y2:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            y1 = y2
            y2 = func(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            y2 = y1
            y1 = func(x1)

    x = (x1 + x2) / 2
    return x


if __name__ == '__main__':
    # a = int(input('Enter left endside: '))
    # b = int(input('Enter right endside: '))
    # eps = float(input('Enter accuracy: '))
    a = -30
    b = 5
    eps = 30
    # n = input('Enter number of iterations for fibonacci method: ')
    # drawGraphic(a, 0, func)
    # drawGraphic(0, b, func)
    drawGraphic(a, b, func)
    print(golden_section(a, b, eps, func))
    # for i in range(15):
    #     temp = float(f'-{i}')
    #     print((i, func(i)), (temp, func(temp)))
    #     print(type(func(i)))
