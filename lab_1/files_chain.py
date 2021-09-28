from abc import ABCMeta, abstractmethod
from typing import Optional


def error_catcher(method):
    def wrapper(*args, **kwargs):
        try:
            return method(*args, *kwargs)
        except (AttributeError, ValueError):
            return "File error: указан неверный тип файла."
    return wrapper


class AbstractHandler(metaclass=ABCMeta):
    """The Interface for handling requests."""

    @abstractmethod
    def set_successor(self, successor):
        """Set the next handler in the chain"""
        pass

    @abstractmethod
    def handle(self, file) -> Optional[str]:
        """Handle the event"""
        pass


class XLSX(AbstractHandler):

    def __init__(self):
        self._successor = None
        self._temp: list = list()

    def set_successor(self, successor):
        self._successor = successor
        return successor

    @error_catcher
    def handle(self, FILE):
        """Handle the *.xlxs file event"""
        file_name, file_ext = str(FILE).split(".")

        if file_ext == self.__class__.__name__.lower():
            with open(FILE, "r") as f:
                print(f.readlines())
                # print(self.__class__.__name__)
            print(self._temp)
            return self.getter()
            # return 'xlsx cheeeeek'
        else:
            return self._successor.handle(FILE)

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def getter(self):
        return self._temp


class TXT(AbstractHandler):

    def __init__(self):
        self._successor = None
        self._temp: list = list()

    def set_successor(self, successor):
        self._successor = successor
        return successor

    @error_catcher
    def handle(self, FILE):
        """Handle the *.txt file event"""
        file_name, file_ext = str(FILE).split(".")

        if file_ext == self.__class__.__name__.lower():
            with open(FILE, "r") as f:
                print(f.readlines())
                for line in f.readlines():
                    pass
                # return f.readlines()
                # print(self.__class__.__name__)
            print(self._temp)
            return self.getter()
            # return 'txt cheeeeek'
        else:
            return self._successor.handle(FILE)

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def getter(self):
        return self._temp


class CSV(AbstractHandler):

    def __init__(self):
        self._successor = None
        self._temp: list = list()

    def set_successor(self, successor):
        self._successor = successor
        return successor

    @error_catcher
    def handle(self, FILE):
        """Handle the *.csv file event"""
        file_name, file_ext = str(FILE).split(".")

        if file_ext == self.__class__.__name__.lower():
            with open(FILE, "r") as f:
                for line in f.read().split(',\n'):
                    reformat_line = line[1:-1].split('","')
                    a = [list(map(float, elem.split(','))) for elem in reformat_line]
                    self._temp.append(a)

            return self.getter()
            # return 'csv cheeeeek'
        else:
            return self._successor.handle(FILE)

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def getter(self):
        return self._temp


class FilesChain:

    def __init__(self):
        self.chain1 = XLSX()
        self.chain2 = TXT()
        self.chain3 = CSV()

        # set the chain of responsibility
        # The Client may compose chains once or
        # the hadler can set them dynamically at
        # handle time
        self.chain1.set_successor(self.chain2).set_successor(self.chain3)

    def client_code(self):
        FILE = str(input("Input file name: "))
        return self.chain1.handle(FILE)
