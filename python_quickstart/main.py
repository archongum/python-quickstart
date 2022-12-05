import sys


def _main():
    print("---------------------------------")
    return "_main"


def main():
    print(_main())
    print(f"__name__: {__name__}")
    print(f"__file__: {__file__}")


if __name__ == "__main__":
    sys.exit(main())
