from typing import Callable

import numpy as np


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
    return round(x, 3), round(func(x), 3), f'Iterations: {iterations}'
