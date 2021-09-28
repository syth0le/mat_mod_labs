from lab_1.files_chain import FilesChain
from lab_1.graphics import Matplotlib, Seaborn, Pandas, Graphics

#
# @Pandas
# @Graphics
@Matplotlib
@Seaborn
def main():
    FILEIO = FilesChain()
    return FILEIO.client_code()


if __name__ == "__main__":
    main()
