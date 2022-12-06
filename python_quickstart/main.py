import sys

from my_script import step1, step2


def main() -> int:
    # 1. xxx
    step1()
    # 2. xxx
    step2()
    # 执行成功
    return 0


if __name__ == "__main__":
    # print(f"[{__file__}] __name__: {__name__}")
    sys.exit(main())
    # main()
