#include <math.h>

/*
    This function calculates the determinant of a 2x2 matrix given the
    trace of the matrix (trace_A) and the trace of its cube (trace_A3).

    The formula is derived from the relationship between the trace,
    determinant, and eigenvalues of a matrix.

    For Windows DLL compilation, __declspec(dllexport) is used to
    export the function, making it visible to other programs. For
    Linux/macOS, this is not strictly necessary when compiling with -fPIC.
*/
#if defined(_WIN32)
    #define DLLEXPORT __declspec(dllexport)
#else
    #define DLLEXPORT
#endif

DLLEXPORT double solve_determinant_2x2(double trace_A, double trace_A3) {
    // Ensure we don't divide by zero if trace_A is 0.
    if (trace_A == 0) {
        return 0.0; // Or handle as an error, e.g., return NAN.
    }
    
    // Formula: det(A) = (tr(A)^3 - tr(A^3)) / (3 * tr(A))
    return (pow(trace_A, 3) - trace_A3) / (3.0 * trace_A);
}

