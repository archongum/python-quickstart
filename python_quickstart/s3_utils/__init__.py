print(f"{__file__}: __name__: {__name__}")

from .obs import get_obs
from .oss import get_oss

__all__ = [
    "get_obs"
    , "get_oss"
]

__version__ = "1.0.0"
