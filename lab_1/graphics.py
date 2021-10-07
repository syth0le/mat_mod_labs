from abc import ABCMeta, abstractmethod
import warnings

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class ABSGraphics(metaclass=ABCMeta):

    def __init__(self, function):
        self.function = function

    @abstractmethod
    def drawGraphic(self, vectors):
        pass


class Pandas(ABSGraphics):

    def drawGraphic(self, vectors):
        colors = plt.rcParams["axes.prop_cycle"]()
        fig, ax = plt.subplots()
        for vector in vectors:
            data = {
                'x': vector[0],
                'y': vector[1]
            }
            df = pd.DataFrame(data, columns=['x', 'y'])
            c = next(colors)["color"]
            df.plot(ax=ax, x='x', y='y', kind='scatter', color=c)

        plt.ylabel('y')
        plt.xlabel('x')
        plt.title('PANDAS GRAPHIC')
        plt.show()
        # points.json

    def __call__(self, *args, **kwargs):
        call = self.function(*args, **kwargs)
        print(self.__class__.__name__)
        self.drawGraphic(call)
        return call


class Matplotlib(ABSGraphics):

    def drawGraphic(self, vectors):

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
