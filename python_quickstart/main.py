import sys


def step1() -> None:
    print("---------------------------------")
    step_name = "step1"
    print(f"Step: {step_name}")


def step2() -> None:
    print("---------------------------------")
    step_name = "step2"
    print(f"Step: {step_name}")


def main() -> int:
    # 1. xxx
    step1()
    # 2. xxx
    step2()
    # 执行成功
    return 0


if __name__ == "__main__":
    sys.exit(main())
