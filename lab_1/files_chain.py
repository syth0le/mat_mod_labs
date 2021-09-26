from abc import ABCMeta, abstractmethod
from typing import Union


class ErrorHandler:

    def __init__(self, method):
        self.method = method

    def __call__(self, *args, **kwargs):
        try:
            self.method(*args, **kwargs)
        except AttributeError:
            print("File error: указан неверный тип файла.")


def error_catcher(method):
    def wrapper(*args, **kwargs):
        try:
            method(*args, *kwargs)
        except AttributeError:
            print("File error: указан неверный тип файла.")
    return wrapper


class AbstractHandler(metaclass=ABCMeta):
    """The Interface for handling requests."""

    @staticmethod
    @abstractmethod
    def set_successor(successor):
        """Set the next handler in the chain"""

    @staticmethod
    @abstractmethod
    def handle(amount):
        """Handle the event"""


class Excel(AbstractHandler):

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    @error_catcher
    def handle(self, smth):
        """Handle the event"""
        if smth == self.__class__.__name__:
            print(self.__class__.__name__)
        else:
            self._successor.handle(smth)

    def __repr__(self):
        return f"{self.__class__.__name__}"


class TXT(AbstractHandler):

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    @error_catcher
    def handle(self, smth):
        """Handle the event"""
        if smth == self.__class__.__name__:
            print(self.__class__.__name__)
        else:
            self._successor.handle(smth)

    def __repr__(self):
        return f"{self.__class__.__name__}"


class CSV(AbstractHandler):

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    @error_catcher
    def handle(self, smth):
        """Handle the event"""
        if smth == self.__class__.__name__:
            print(self.__class__.__name__)
        else:
            self._successor.handle(smth)

    def __repr__(self):
        return f"{self.__class__.__name__}"


class FilesChain:

    def __init__(self):
        self.chain1 = Excel()
        self.chain2 = TXT()
        self.chain3 = CSV()

        # set the chain of responsibility
        # The Client may compose chains once or
        # the hadler can set them dynamically at
        # handle time
        self.chain1.set_successor(self.chain2)
        self.chain2.set_successor(self.chain3)


if __name__ == "__main__":
    chain = FilesChain()

    file = str(input("Input file name: "))
    chain.chain1.handle(file)
