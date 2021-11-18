import numpy as np
from matplotlib import pyplot as plt

from utils.delimeter import Delimeter
from utils.files_chain import FilesChain
from utils.sorting import bubble_sort


class Approximation:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        call = self.function()
        self.drawGraphic(call)
        return call

    def drawGraphic(self, vectors):
        print("Введите степень аппроксимирующего полинома:")
        degree = int(input())
        for vector in vectors:
            vector = bubble_sort(vector)
            x = vector[0]
            y = vector[1]
            self.approximation(x, y, degree)
            plt.scatter(x, y)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Approximation")
        plt.show()

    def approximation(self, x, y, degree):
        fp, residuals, rank, sv, rcond = np.polyfit(x, y, degree, full=True)
        f = np.poly1d(fp)
        fx = np.linspace(np.min(x), np.max(x), 10000)
        plt.plot(fx, f(fx))
        plt.grid(True)


@Approximation
@Delimeter
def main():
    FILEIO = FilesChain()
    return FILEIO.client_code()


if __name__ == "__main__":
    main()
