from abc import ABCMeta, abstractmethod


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


class XLSX(AbstractHandler):

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    @error_catcher
    def handle(self, FILE):
        """Handle the event"""
        file_name, file_ext = str(FILE).split(".")

        if file_ext == self.__class__.__name__.lower():
            with open(FILE, "r") as f:
                print(f.readlines())
                # print(self.__class__.__name__)
        else:
            self._successor.handle(FILE)

    def __repr__(self):
        return f"{self.__class__.__name__}"


class TXT(AbstractHandler):

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    @error_catcher
    def handle(self, FILE):
        """Handle the event"""
        file_name, file_ext = str(FILE).split(".")

        if file_ext == self.__class__.__name__.lower():
            with open(FILE, "r") as f:
                print(f.readlines())
                # print(self.__class__.__name__)
        else:
            self._successor.handle(FILE)

    def __repr__(self):
        return f"{self.__class__.__name__}"


class CSV(AbstractHandler):

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    @error_catcher
    def handle(self, FILE):
        """Handle the event"""
        file_name, file_ext = str(FILE).split(".")

        if file_ext == self.__class__.__name__.lower():
            with open(FILE, "r") as f:
                print(f.readlines())
                # print(self.__class__.__name__)
        else:
            self._successor.handle(FILE)

    def __repr__(self):
        return f"{self.__class__.__name__}"


class FilesChain:

    def __init__(self):
        self.chain1 = XLSX()
        self.chain2 = TXT()
        self.chain3 = CSV()

        # set the chain of responsibility
        # The Client may compose chains once or
        # the hadler can set them dynamically at
        # handle time
        self.chain1.set_successor(self.chain2)
        self.chain2.set_successor(self.chain3)


# def main():
if __name__ == "__main__":
    FILEIO = FilesChain()

    file = str(input("Input file name: ")) # points.txt for example
    FILEIO.chain1.handle(file)
