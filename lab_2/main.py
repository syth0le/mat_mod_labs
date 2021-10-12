from lab_2.graphics import *
from utils.delimeter import Delimeter
from utils.files_chain import FilesChain


@InterpolationSpline
@InterpolationParabolic
@InterpolationLinear
@Lagranz
@Delimeter
def main():
    FILEIO = FilesChain()
    return FILEIO.client_code()


if __name__ == "__main__":
    main()
