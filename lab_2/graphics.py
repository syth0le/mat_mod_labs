import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
from abc import ABCMeta, abstractmethod

from utils.sorting import bubble_sort


class ABSMethods(metaclass=ABCMeta):
    def __init__(self, function):
        self.function = function

    @abstractmethod
    def drawGraphic(self, vectors):
        pass


class Lagranz(ABSMethods):

    def __call__(self, *args, **kwargs):
        call = self.function()
        self.drawGraphic(call)
        return call

    def counter(self, x, y, xl):
        z = 0
        for j in range(len(y)):
            p1 = 1
            p2 = 1
            for i in range(len(x)):
                if i == j:
                    p1 = p1 * 1
                    p2 = p2 * 1
                else:
                    p1 = p1 * (xl - x[i])
                    p2 = p2 * (x[j] - x[i])
            z = z + y[j] * p1 / p2
        return z

    def drawGraphic(self, vectors):

        for vector in vectors:
            vector = bubble_sort(vector)
            x = vector[0]
            y = vector[1]
            xl = np.linspace(np.min(x), np.max(x))
            yl = self.counter(x, y, xl)
            plt.scatter(x, y)
            plt.plot(xl, yl)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Lagranz Method")
        plt.show()


class InterpolationLinear(ABSMethods):

    def __call__(self, *args, **kwargs):
        call = self.function()
        self.drawGraphic(call)
        return call

    def counter(self, x, y, xl):
        yx = 0
        for i in range(len(x)):
            if x[i - 1] <= xl <= x[i]:
                yp = y[i] - y[i - 1]
                xp = x[i] - x[i - 1]
                yx = y[i] + ((yp / xp) * (xl - x[i]))
                break
        return yx

    def drawGraphic(self, vectors):
        for vector in vectors:
            vector = bubble_sort(vector)
            x = vector[0]
            y = vector[1]
            yl = [self.counter(x, y, i) for i in x]
            plt.scatter(x, y)
            plt.plot(x, yl)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Piecewise linear interpolation Method")
        plt.show()


class InterpolationParabolic(ABSMethods):

    def __call__(self, *args, **kwargs):
        call = self.function()
        self.drawGraphic(call)
        return call

    def counter(self, x, y, t):
        z = 0
        for i in range(len(x) - 1):
            if x[i] <= t <= x[i + 1]:
                M = np.array(
                    [[x[i - 1] ** 2, x[i - 1], 1], [x[i] ** 2, x[i], 1], [x[i + 1] ** 2, x[i + 1], 1]])
                v = np.array([y[i - 1], y[i], y[i + 1]])
                solve = np.linalg.solve(M, v)
                z = solve[0] * t ** 2 + solve[1] * t + solve[2]
            i += 1
        return z

    def drawGraphic(self, vectors):
        for vector in vectors:
            vector = bubble_sort(vector)
            x = vector[0]
            y = vector[1]
            plt.scatter(x, y)
            xnew = np.linspace(np.min(x), np.max(x), 10000)
            ynew = [self.counter(x, y, i) for i in xnew]
            plt.plot(xnew, ynew)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Piecewise parabolic interpolation Method")
        plt.show()


class InterpolationSpline(ABSMethods):

    def __call__(self, *args, **kwargs):
        call = self.function()
        self.drawGraphic(call)
        return call

    def counter(self, x, y):
        tck = interpolate.splrep(x, y, s=0)
        xl = np.linspace(np.min(x), np.max(x))
        yl = interpolate.splev(xl, tck, der=0)
        return xl, yl

    def drawGraphic(self, vectors):
        for vector in vectors:
            vector = bubble_sort(vector)
            x = vector[0]
            y = vector[1]
            xl, yl = self.counter(x, y)
            plt.scatter(x, y)
            plt.plot(xl, yl)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Spline interpolation Method")
        plt.show()


class Graphics(ABSMethods):

    def __call__(self, *args, **kwargs):
        # call = self.function()
        # print(call)
        call = 0
        self.drawGraphic(call)
        return call

    def drawGraphic(self, call):
        print("\n1 - Lagranz\n2 - Linear\n3 - Parabolic\n4 - Spline")
        command = int(input("Введите номер задания (из методички):"))
        if command == 1:
            meth = Lagranz(self.function)
            meth()
        elif command == 2:
            meth = InterpolationLinear(self.function)
            meth()
        elif command == 3:
            meth = InterpolationParabolic(self.function)
            meth()
        elif command == 4:
            meth = InterpolationSpline(self.function)
            meth()
        else:
            print("Invalid command")
