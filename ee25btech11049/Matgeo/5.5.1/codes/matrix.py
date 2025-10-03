import ctypes
import numpy as np
import sympy as sp

# Load C library
lib = ctypes.CDLL("./matrix.so")

# Define function signature
lib.inverse.argtypes = [ctypes.POINTER((ctypes.c_double * 3) * 3),
                        ctypes.POINTER((ctypes.c_double * 3) * 3)]

# Input matrix
A = np.array([[5, -1, 4],
              [2, 3, 5],
              [5, -2, 6]], dtype=np.double)

inv = np.zeros((3,3), dtype=np.double)

# Call C function
lib.inverse(A.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 3) * 3)),
            inv.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 3) * 3)))

inverse=sp.Matrix(inv)
sp.pprint(inverse)
