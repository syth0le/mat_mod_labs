from math import sqrt

import numpy as np


def fibonacci(n: int) -> float:
    """
    Function that returns value of n number of Fibonacci sequence.
    Args:
        n (int): number of Fibonacci sequence.
    Returns:
        float: value of n number of Fibonacci sequence.
    """
    return \
        (pow((1 + sqrt(5)) / 2, n + 1) - pow((1 - sqrt(5)) / 2, n + 1)) / sqrt(5)


def get_iterations_quantity(a: float, b: float, fidelity: float) -> int:
    """
    Function that returns iterations quantity for Fibonacci method.
    Args:
        a (float): left border of the search range;
        b (float): right border of the search range;
        fidelity (float): fidelity of extremum calculation.
    Returns:
        int: iterations quantity.
    """
    k = (b - a) / fidelity
    n = 0
    while fibonacci(n) <= k: n += 1

    return n


def fibonacci_method(function, a: float, b: float, x1: float,
                     x2: float, n: int) -> float:
    """
    Recursive function that returns extremum of function in specified range
    [a, b] with n recursion depth.
    Args:
        function (function): python function like lambda x: x * 2;
        a (float): starting point of the search interval;
        b (float): ending point of the search interval;
        x1 (float): first starting point of division;
        x2 (float): second starting point of division;
        n (int): recursion depth.
    Returns:
        float: extremum point of function.
    """
    if n == 1:
        return (x1 + x2) / 2

    if function(x1) > function(x2):
        a = x1
        x1 = x2
        x2 = b - x1 + a
    else:
        b = x2
        x2 = x1
        x1 = a + b - x2

    return fibonacci_method(function,
                            a,
                            b,
                            x1,
                            x2,
                            n - 1)


def get_extremum_of_function_by_fibonacci_method(function, a, b, fidelity) -> \
        float:
    """
    Function that returns extremum of function by Fibonacci method.
    Args:
        function (function): python function like lambda x: x * 2;
        a (float): starting point of the search interval;
        b (float): ending point of the search interval;
        fidelity(float): fidelity of extremum calculation.
    Returns:
        float: extremum point of function.
    """
    n = get_iterations_quantity(a, b, fidelity)
    x1 = a + (b - a) * fibonacci(n - 2) / fibonacci(n)
    x2 = a + (b - a) * fibonacci(n - 1) / fibonacci(n)

    return fibonacci_method(function, a, b, x1, x2, n)


func = lambda x: x ** 2 + 2 * np.exp(x)
a = -30
b = 5
fidelity = 1e-5

print(get_extremum_of_function_by_fibonacci_method(func, a, b, fidelity))
