import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

# --- Parameters ---
a = 5.0
b = 3.0
theta = np.pi / 6
phi = np.pi / 2 - theta

# --- Hyperbola Representation (Matrix Form) ---
# The hyperbola equation b^2*x^2 - a^2*y^2 - a^2*b^2 = 0 can be written as:
# g(x) = x.T @ V @ x + 2*u.T @ x + f = 0
V = np.array([[b**2, 0], [0, -a**2]])
u = np.zeros((2, 1))
f = -(a**2) * (b**2)

# Define the 90-degree rotation matrix R
R = np.array([[0, -1], [1, 0]])

# --- Points on Hyperbola ---
P = np.array([[a / np.cos(theta)], [b * np.tan(theta)]])
Q = np.array([[a / np.cos(phi)], [b * np.tan(phi)]])

#
# --- Derivation of Normals ---
#
# The equation of the normal at a point 'q' is given by:
# (V*q + u).T @ R @ (x - q) = 0
# This can be rewritten as a linear equation: A*x + B*y = C
#

# Normal at Point P
# Let the coefficient vector be M_P = (V*P + u).T @ R
grad_P = V @ P + u
M_P = (grad_P.T @ R).flatten()
C1 = M_P @ P.flatten()

# Normal at Point Q
# Let the coefficient vector be M_Q = (V*Q + u).T @ R
grad_Q = V @ Q + u
M_Q = (grad_Q.T @ R).flatten()
C2 = M_Q @ Q.flatten()

#
# --- Solving for Intersection Point (h, k) ---
#
# We now have a system of two linear equations:
# M_P[0]*h + M_P[1]*k = C1
# M_Q[0]*h + M_Q[1]*k = C2
#

A_matrix = np.vstack((M_P, M_Q))
B_vector = np.array([C1, C2])

# Solve the system A*x = B for x = [h, k]
intersection_point = LA.solve(A_matrix, B_vector)
h, k = intersection_point[0], intersection_point[1]

# --- Verification ---
# The analytical result from main.tex is k = -(a^2 + b^2)/b
k_theoretical = -(a**2 + b**2) / b

# --- Output Results ---
print("--- Hyperbola and Points ---")
print(f"Equation: x^2/{a**2:.1f} - y^2/{b**2:.1f} = 1")
print(f"Point P(theta={theta:.2f} rad): ({P[0,0]:.2f}, {P[1,0]:.2f})")
print(f"Point Q(phi  ={phi:.2f} rad): ({Q[0,0]:.2f}, {Q[1,0]:.2f})")
print("\n--- Intersection of Normals ---")
print(f"Intersection point (h, k): ({h:.2f}, {k:.2f})")
print(f"Value of k from numerical solution: {k:.4f}")
print(f"Theoretical value k = -(a^2+b^2)/b: {k_theoretical:.4f}")

#
# --- Plotting ---
#
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, aspect='equal')

# Generate points for the hyperbola using parametric form
t = np.linspace(-2, 2, 400)
x_hyperbola_right = a * np.cosh(t)
y_hyperbola = b * np.sinh(t)
x_hyperbola_left = -x_hyperbola_right

# Plot the hyperbola
ax.plot(x_hyperbola_right, y_hyperbola, 'r', label='Hyperbola')
ax.plot(x_hyperbola_left, y_hyperbola, 'r')

# Plot the points P, Q, and the intersection point
ax.plot(P[0], P[1], 'go', markersize=8, label=f'P ({P[0,0]:.1f}, {P[1,0]:.1f})')
ax.plot(Q[0], Q[1], 'bo', markersize=8, label=f'Q ({Q[0,0]:.1f}, {Q[1,0]:.1f})')
ax.plot(h, k, 'kX', markersize=10, label=f'Intersection (h,k) ({h:.1f}, {k:.1f})')

# Function to plot a line given its equation Ax + By = C
def plot_line(coeffs, const, x_range, style, label):
    A, B = coeffs[0], coeffs[1]
    # To handle vertical lines where B=0
    if np.abs(B) < 1e-6:
        x_points = np.full_like(x_range, const/A)
        y_points = np.linspace(min(ax.get_ylim()), max(ax.get_ylim()), len(x_range))
    else:
        x_points = np.array(x_range)
        y_points = (const - A * x_points) / B
    ax.plot(x_points, y_points, style, label=label)

# Define a suitable range for plotting the normal lines
plot_range = (min(P[0,0], Q[0,0], h) - 5, max(P[0,0], Q[0,0], h) + 5)

# Plot the normal lines
plot_line(M_P, C1, plot_range, 'g--', 'Normal at P')
plot_line(M_Q, C2, plot_range, 'b--', 'Normal at Q')

# --- Plot Formatting ---
# Set axis spines to pass through the origin
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Set labels and legend
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper left')
plt.grid(True)

# Set plot limits to ensure all points are visible
xlim_max = max(abs(P[0,0]), abs(Q[0,0]), abs(h)) + 4
ylim_max = max(abs(P[1,0]), abs(Q[1,0]), abs(k)) + 4
plt.xlim(-xlim_max, xlim_max)
plt.ylim(-ylim_max, ylim_max)

# Show the plot
plt.show()
