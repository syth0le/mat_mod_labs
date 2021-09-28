from abc import ABCMeta, abstractmethod
import warnings
from matplotlib import pyplot as plt
from pandas import DataFrame
import seaborn as sns


class ABSGraphics(metaclass=ABCMeta):

    def __init__(self, function):
        self.function = function

    @abstractmethod
    def drawGraphic(self, vectors):
        pass


class Pandas(ABSGraphics):

    def drawGraphic(self, vectors):
        for vector in vectors:
            x = vector[0]
            y = vector[1]
        df = DataFrame(vectors, columns=['x', 'y'])
        df.plot(kind='scatter', data=df, s=120)
        plt.title("PANDAS GRAPHIC")
        plt.show()

    def __call__(self, *args, **kwargs):
        call = self.function(*args, **kwargs)
        print(self.__class__.__name__)
        self.drawGraphic(call)
        return call


class Matplotlib(ABSGraphics):

    def drawGraphic(self, vectors):
        # print(vectors)
        for vector in vectors:
            x = vector[0]
            y = vector[1]
            plt.scatter(x, y)
        plt.title("MATPLOTLIB GRAPHIC")
        plt.show()

    def __call__(self, *args, **kwargs):
        call = self.function(*args, **kwargs)
        print(self.__class__.__name__)
        self.drawGraphic(call)
        return call


class Seaborn(ABSGraphics):

    def drawGraphic(self, vectors):
        warnings.simplefilter(action="ignore", category=FutureWarning)
        for vector in vectors:
            x = vector[0]
            y = vector[1]
            sns.scatterplot(x=x, y=y)
        plt.title("SEABORN GRAPHIC")
        plt.show()

    def __call__(self, *args, **kwargs):
        call = self.function(*args, **kwargs)
        print(self.__class__.__name__)
        self.drawGraphic(call)
        return call


class Graphics:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # choose class of graphics
        # do initialization if class and do some work
        rez = self.func()
        plt.show()
