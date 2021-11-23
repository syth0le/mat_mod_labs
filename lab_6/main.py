from typing import Callable

import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

# https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%B7%D0%BE%D0%BB%D0%BE%D1%82%D0%BE%D0%B3%D0%BE_%D1%81%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F


func = lambda x: x ** 2 + 2 * np.exp(x)


# так как у функция возврастающая на положительных иксах и убывающая на отрицательных
# проще найти минимумы


def drawGraphic(a, b, func):
    x = np.linspace(a, b, 10000)
    sns.set_theme(style="darkgrid")
    sns.lineplot(x, func(x))
    plt.show()


def golden_section(func: Callable, a: int, b: int, eps=1e-5) -> tuple:
    iterations = 0
    fi = (1 + np.sqrt(5)) / 2  # пропорция золотого сечения
    x1 = b - (b - a) / fi
    x2 = a + (b - a) / fi

    while abs(b - a) > eps:
        if func(x1) < func(x2):
            b = x2
        else:
            a = x1

        x1 = b - (b - a) / fi
        x2 = a + (b - a) / fi
        iterations += 1

    x = (a + b) / 2
    return x, func(x), f'Iterations: {iterations}'


def fibonacci_method(func: Callable, a: int, b: int, n: int):
    x1 = a + (b - a) * fibonacci_method(a, b, n - 2, func) / fibonacci_method(a, b, n, func)
    x2 = a + (b - a) * fibonacci_method(a, b, n - 1, func) / fibonacci_method(a, b, n, func)
    y1 = func(x1)
    y2 = func(x2)
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
    return x, func(x), \
        # f'Iterations: {iterations}'


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
    # drawGraphic(a, b, func)
    print(golden_section(func, a, b, eps))
    print(golden_section(func, a, b))

    print(fibonacci_method(func, a, b, 10))
    # for i in range(15):
    #     temp = float(f'-{i}')
    #     print((i, func(i)), (temp, func(temp)))
    #     print(type(func(i)))
