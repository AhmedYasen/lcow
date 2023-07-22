import argparse
from ls import LsCmd

def main():
    parser = argparse.ArgumentParser(description="Delete files/directories with options.")
    parser.add_argument("paths", help="Path of the file or directory to delete.", nargs="*", default=[])
    parser.add_argument("-a", "--all",
                        help="do not ignore entries starting with .")
    args = parser.parse_args()

    LsCmd(args)


if __name__ == "__main__":
    main()