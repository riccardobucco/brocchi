"""
Function name: matrix_mul

This function computes the product of two matrices.

Matrix multiplication: https://en.wikipedia.org/wiki/Matrix_multiplication
Matrix multiplication is a binary operation that takes a pair of matrices, and produces another matrix.
If A is an n x m matrix and B is an m x p matrix, the result of their multiplication is an n x p matrix.

How to multiply two matrices:
The element C[i][j] is the dot product of the i-th row of matrix A and the j-th column of matrix B.
The dot product of two vectors is the sum of the products of the corresponding elements of the two vectors.
Example: https://www.mathsisfun.com/algebra/matrix-multiplying.html

Arguments:
- A: a list of lists of numbers (n x m matrix).
- B: a list of lists of numbers (m x p matrix).

Returns:
The product of matrices A and B (an n x p matrix).

Examples:
matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]]) returns [[19, 22], [43, 50]].
matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]) returns [[58, 64], [139, 154]].
"""

def matrix_mul(A, B):
    # START CODE HERE
    # END CODE HERE
    return matrix_product


from test_cases import test_matrix_mul

test_matrix_mul(matrix_mul)
