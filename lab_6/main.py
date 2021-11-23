import numpy as np

from draw_graphic import drawGraphic
from fibonacci import get_extremum_of_function_by_fibonacci_method
from golden_section import golden_section
from table import print_table

func = lambda x: x ** 2 + 2 * np.exp(x)
# так как у функция возврастающая на положительных иксах и убывающая на отрицательных
# проще найти минимумы


if __name__ == '__main__':
    a = int(input('Enter left endside: '))
    b = int(input('Enter right endside: '))
    eps = float(input('Enter accuracy: '))
    qa = input('Do u want to set N - number of iterations for fibonacci method [y/n]: ')
    if qa == 'y':
        n = int(input('Enter number of iterations for fibonacci method: '))
    else:
        n = None

    gss = golden_section(func, a, b, eps)
    fib = get_extremum_of_function_by_fibonacci_method(func, a, b, eps, n)
    print_table(gss, fib)
    drawGraphic(a, b, func)
