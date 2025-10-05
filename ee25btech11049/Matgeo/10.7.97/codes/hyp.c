#include <math.h>

// Define a structure to return the (x, y) coordinates
struct Point {
    double x;
    double y;
};

// This function will be exported to the shared library
// It takes hyperbola parameters a, b, and the angle theta
struct Point find_intersection(double a, double b, double theta) {
    // Given condition from the problem
    double phi = M_PI / 2.0 - theta;

    // Coefficients for the equation of the normal at P(theta)
    // from a*tan(theta)*h + b*sec(theta)*k = (a^2+b^2)*tan(theta)*sec(theta)
    double A1 = a * tan(theta);
    double B1 = b / cos(theta);
    double C1 = (a * a + b * b) * tan(theta) / cos(theta);

    // Coefficients for the equation of the normal at Q(phi)
    // from a*tan(phi)*h + b*sec(phi)*k = (a^2+b^2)*tan(phi)*sec(phi)
    double A2 = a * tan(phi);
    double B2 = b / cos(phi);
    double C2 = (a * a + b * b) * tan(phi) / cos(phi);

    // Solve the 2x2 system of linear equations for h (intersection.x) and k (intersection.y)
    // A1*h + B1*k = C1
    // A2*h + B2*k = C2
    // Using Cramer's rule:
    double determinant = A1 * B2 - A2 * B1;
    
    struct Point intersection;

    if (determinant != 0) {
        intersection.x = (C1 * B2 - C2 * B1) / determinant;
        intersection.y = (A1 * C2 - A2 * C1) / determinant;
    } else {
        // This case (parallel normals) shouldn't occur for a hyperbola
        intersection.x = NAN; // Not a Number
        intersection.y = NAN;
    }

    return intersection;
}
