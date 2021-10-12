from lab_1.graphics import Matplotlib, Seaborn, Pandas
from utils.delimeter import Delimeter
from utils.files_chain import FilesChain


@Pandas
@Seaborn
@Matplotlib
@Delimeter
def main():
    FILEIO = FilesChain()
    return FILEIO.client_code()


if __name__ == "__main__":
    main()
