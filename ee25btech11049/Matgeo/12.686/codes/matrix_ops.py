# use_c_from_python.py
# This script demonstrates how to call a C function from Python using the ctypes library.
# It uses the `calculate_D` function from the compiled `matrix_ops.so` or `matrix_ops.dll` library.

import ctypes
import random
import os

# --- Compilation Instructions ---
# Before running this script, you must compile the C code into a shared library.
# The command depends on your operating system.
#
# For Linux or macOS:
# gcc -shared -o matrix_ops.so -fPIC matrix_ops.c
#
# For Windows (using MinGW/GCC):
# gcc -shared -o matrix_ops.dll matrix_ops.c
# --------------------------------

# Determine the library file name based on the OS
lib_name = 'matrix_ops.so' if os.name != 'nt' else 'matrix_ops.dll'
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_name)

# 1. Load the shared library
try:
    c_lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading shared library: {e}")
    print("Please make sure you have compiled `matrix_ops.c` into a shared library.")
    exit()

# 2. Define the function signature (argument types and return type)
# The function is: void calculate_D(int* A, int* B, int* C, int* D)
# We need to specify that the arguments are pointers to integers.
IntArray4 = ctypes.c_int * 4
c_lib.calculate_D.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int)
]
c_lib.calculate_D.restype = None  # The C function returns void

# 3. Prepare the data in Python
# Generate random vectors A, B, and C
A_py = [random.randint(1, 10) for _ in range(4)]
B_py = [random.randint(1, 10) for _ in range(4)]
C_py = [random.randint(1, 10) for _ in range(4)]

# Convert Python lists to C-compatible integer arrays
A_c = IntArray4(*A_py)
B_c = IntArray4(*B_py)
C_c = IntArray4(*C_py)

# Create an empty C array to store the result D
D_c = IntArray4()

# 4. Call the C function
c_lib.calculate_D(A_c, B_c, C_c, D_c)

# 5. Convert the result back to a Python list to display it
D_py = list(D_c)

# Print the results
print("--- Using C function from Python (ctypes) ---")
print(f"Vector A: {A_py}")
print(f"Vector B: {B_py}")
print(f"Vector C: {C_py}")
print(f"Result D (3*A + 2*B + C): {D_py}")

# Verification
D_verify = [(3 * a + 2 * b + c) for a, b, c in zip(A_py, B_py, C_py)]
print(f"Verification in Python: {D_verify}")
assert D_py == D_verify
print("Result matches Python's calculation.")

