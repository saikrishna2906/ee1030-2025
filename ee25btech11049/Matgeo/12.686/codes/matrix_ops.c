/**
 * @file matrix_ops.c
 * @brief A C library to perform vector operations.
 *
 * This code defines a function to calculate a resultant vector D based on the
 * linear combination of three input vectors A, B, and C, according to the
 * formula D = 3*A + 2*B + C.
 */

#include <stdio.h>

// Define the length of the vectors.
#define VECTOR_LENGTH 4

/**
 * @brief Calculates vector D as a linear combination of vectors A, B, and C.
 *
 * This function takes three source vectors (A, B, C) and calculates a
 * destination vector (D) where each element is computed as:
 * D[i] = 3 * A[i] + 2 * B[i] + C[i].
 *
 * @param A Pointer to the first integer array (vector A).
 * @param B Pointer to the second integer array (vector B).
 * @param C Pointer to the third integer array (vector C).
 * @param D Pointer to the output integer array (vector D), which will be modified.
 */
void calculate_D(const int* A, const int* B, const int* C, int* D) {
    for (int i = 0; i < VECTOR_LENGTH; i++) {
        D[i] = (3 * A[i]) + (2 * B[i]) + C[i];
    }
}

