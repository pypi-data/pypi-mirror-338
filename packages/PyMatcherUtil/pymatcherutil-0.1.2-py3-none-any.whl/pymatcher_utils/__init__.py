from pymatcher_utils.array import *
from pymatcher_utils.dict import *
from pymatcher_utils.exception import *
from pymatcher_utils.matcher import *
from pymatcher_utils.method import *
from pymatcher_utils.property import *

try:
    from importlib.metadata import version, PackageNotFoundError

    __version__ = version("pymatcher_utils")
except PackageNotFoundError:
    # fallback to unknown version
    __version__ = "0.0.0"

__author__ = "Akito Nozaki"
__copyright__ = "Copyright (c) 2024 Akito Nozaki"
__license__ = "MIT"

__all__ = [
    "Matcher",
    "ArrayEq",
    "DictEq",
    "RaiseError",
    "All",
    "Eq",
    "NotEq",
    "Is",
    "IsNot",
    "IsInstance",
    "Called",
    "NotCalled",
    "PropEq",
    "check_value",
    "set_properties",
    "check_properties",
]
