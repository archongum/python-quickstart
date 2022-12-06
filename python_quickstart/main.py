import sys

from .s3_utils import get_obs, get_oss


def main() -> None:
    print("---------------------------------")
    print(f"{__file__}: __name__: {__name__}")
    print(get_obs())
    print(get_oss())
