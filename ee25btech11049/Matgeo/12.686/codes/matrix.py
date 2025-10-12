# Code modified to solve the specified rank problem.
# It demonstrates finding the rank of a matrix where one column
# is a linear combination of the others.

import numpy as np
import numpy.linalg as LA

# 1. Define three linearly independent vectors A, B, and C of length 4.
#    A simple choice is to use vectors with a single non-zero element.
A = np.array([[1], [0], [0], [0]])
B = np.array([[0], [1], [0], [0]])
C = np.array([[0], [0], [1], [0]])

# 2. Define vector D as a linear combination of A, B, and C, as per the problem.
#    D = 3A + 2B + C
D = 3 * A + 2 * B + C

# 3. Construct the matrix M by combining the vectors as columns.
M = np.concatenate((A, B, C, D), axis=1)

# 4. Calculate the rank of the matrix M.
#    The rank is the maximum number of linearly independent columns.
#    Since D is dependent on A, B, and C, the rank should be 3.
rank_of_M = LA.matrix_rank(M)

# Print the vectors, the resulting matrix, and its rank for verification.
print("--- VECTORS ---")
print("Vector A:\n", A)
print("\nVector B:\n", B)
print("\nVector C:\n", C)
print("\nVector D = 3A + 2B + C:\n", D)

print("\n--- MATRIX [A B C D] ---")
print(M)

print("\n--- RESULT ---")
print(f"The rank of the matrix is: {rank_of_M}")
