import sys
from pathlib import Path
sys.path.insert(0, Path(__name__).parent.absolute().as_posix())
print(sys.path)

import python_quickstart.s3_utils as s3_utils
print(s3_utils.get_oss())
