import sys

from s3_utils import get_obs, get_oss
# from s3_utils.obs import get_obs
# from s3_utils.oss import get_oss
# from s3_utils import *


def main() -> int:
    print("---------------------------------")
    print(f"{__file__}: __name__: {__name__}")
    print(get_obs())
    print(get_oss())
    return 0


if __name__ == "__main__":
    sys.exit(main())
