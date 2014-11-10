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

from ctypes import *
mpi = CDLL('libmpi.so.1', RTLD_GLOBAL)
f = pythonapi.Py_GetArgcArgv
argc = c_int()
argv = POINTER(c_char_p)()
f(byref(argc), byref(argv))
mpi.MPI_Init(byref(argc), byref(argv))

# verbose messages from the C interface
set_loglevel(2)

