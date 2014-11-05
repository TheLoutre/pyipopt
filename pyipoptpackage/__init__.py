"""
This is a package for a python interface to ipopt.

The underlying C interface is in pyipoptcore.
"""
import os
import sys

sys.path.append(os.path.dirname(__file__))

import functools

import numpy

from ipoptconst import *
from pyipoptcore import *
from ipoptunconstrained import fmin_unconstrained

# verbose messages from the C interface
import ctypes
ctypes.CDLL('libmpi.so.1', ctypes.RTLD_GLOBAL)
set_loglevel(2)

