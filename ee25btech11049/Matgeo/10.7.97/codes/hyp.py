import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- 1. SETUP CTYPES INTERFACE ---

# Define a Python class that mirrors the C 'struct Point'.
# This tells Python how to interpret the data returned by the C function.
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

# Load the compiled C shared library.
# The name must match the file created in the compilation step.
# On Windows, this would be 'intersection.dll'.
# On macOS, it would be 'intersection.dylib'.
try:
    c_lib = ctypes.CDLL('./hyp.so')
except OSError:
    print("Could not load the C library.")
    print("Please make sure you have compiled 'intersection.c' into 'intersection.so'")
    exit()

# Define the function signature from the C library for type safety.
# Set the return type of the C function to be our Point structure.
c_lib.find_intersection.restype = Point
# Set the argument types for the C function (three doubles).
c_lib.find_intersection.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]


# --- 2. PYTHON LOGIC AND VISUALIZATION ---

# Parameters (chosen to match the plot in Figure_1.png)
a = 5.0
b = 3.0
theta = 0.52

# --- Call the C function to perform the calculation ---
# The heavy lifting is now done by the compiled C code.
intersection_result = c_lib.find_intersection(a, b, theta)
h = intersection_result.x
k = intersection_result.y

# --- Verification ---
# Compare the result from C with the theoretical value from main.tex
k_theoretical = -(a**2 + b**2) / b
print("--- Intersection of Normals (Calculated in C) ---")
print(f"Intersection point (h, k) from C: ({h:.4f}, {k:.4f})")
print(f"Theoretical value for k:            {k_theoretical:.4f}")

# --- Plotting ---
# The rest of the code uses the results from C to generate the plot.
phi = np.pi / 2 - theta
P = np.array([a / np.cos(theta), b * np.tan(theta)])
Q = np.array([a / np.cos(phi), b * np.tan(phi)])

fig, ax = plt.subplots(figsize=(12, 10))

# Plot hyperbola
t = np.linspace(-1.8, 1.8, 400)
x_hyperbola = a * np.cosh(t)
y_hyperbola = b * np.sinh(t)
ax.plot(x_hyperbola, y_hyperbola, 'r', label='Hyperbola')
ax.plot(-x_hyperbola, y_hyperbola, 'r')

# Plot points and the intersection point calculated by C
ax.plot(P[0], P[1], 'go', markersize=8, label=f'P ({P[0]:.1f}, {P[1]:.1f})')
ax.plot(Q[0], Q[1], 'bo', markersize=8, label=f'Q ({Q[0]:.1f}, {Q[1]:.1f})')
ax.plot(h, k, 'kX', markersize=10, mew=2, label=f'Intersection (h,k) ({h:.1f}, {k:.1f})')

# Plot normal lines using the same equations for visualization
x_line_range = np.linspace(0, h + 2, 100)
A1 = a * np.tan(theta)
B1 = b / np.cos(theta)
C1 = (a**2 + b**2) * np.tan(theta) / np.cos(theta)
y_vals_P = (C1 - A1 * x_line_range) / B1
ax.plot(x_line_range, y_vals_P, 'g--', label='Normal at P')

A2 = a / np.tan(theta)
B2 = b / np.sin(theta)
C2 = (a**2 + b**2) / (np.tan(theta) * np.sin(theta))
y_vals_Q = (C2 - A2 * x_line_range) / B2
ax.plot(x_line_range, y_vals_Q, 'b--', label='Normal at Q')

# Formatting to match the desired figure
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlabel('x', loc='right')
ax.set_ylabel('y', loc='top', rotation=0, labelpad=-10)
ax.legend(loc='upper left')
ax.grid(True)
ax.set_xlim(-25, 25)
ax.set_ylim(-15, 15)
ax.set_aspect('equal', adjustable='box')

plt.show()

