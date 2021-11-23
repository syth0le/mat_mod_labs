import numpy as np

from draw_graphic import drawGraphic
from fibonacci import get_extremum_of_function_by_fibonacci_method
from golden_section import golden_section

func = lambda x: x ** 2 + 2 * np.exp(x)

# так как у функция возврастающая на положительных иксах и убывающая на отрицательных
# проще найти минимумы


if __name__ == '__main__':
    a = int(input('Enter left endside: '))
    b = int(input('Enter right endside: '))
    eps = float(input('Enter accuracy: '))
    n = input('Enter number of iterations for fibonacci method: ')
    drawGraphic(a, b, func)
    print(golden_section(func, a, b, eps))
    print(get_extremum_of_function_by_fibonacci_method(func, a, b, eps))
