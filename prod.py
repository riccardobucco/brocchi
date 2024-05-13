"""
Function name: prod_

This function computes the product of two numbers, or two lists of numbers, or a number and a list of numbers, or a number and a list of lists of numbers, or two lists of lists of numbers.
The function should return the same result if the order of the arguments is swapped,
i.e. prod_(A, B) should return the same result as prod_(B, A) (the function is commutative).

Elemetwise matrix multiplication: https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
The Hadamard product (also known as the element-wise product, entrywise product or Schur product) is a binary operation
that takes in two matrices of the same dimensions and returns a matrix of the multiplied corresponding elements.

Arguments:
- A: a number, or a list of numbers, or a list of lists of numbers.
- B: a number, or a list of numbers, or a list of lists of numbers.

Returns:
- If A and B are numbers, the function returns the product of A and B.
- If A is a number and B is a list of numbers, the function returns a list of products of A and the numbers in B.
- If A is a list of lists of numbers and B is number, the function returns a list of lists of products of the numbers in A and B.
- If A and B are lists of numbers, the function returns a list of products of the numbers in A and B. The lists must have the same length.
- If A and B are lists of lists of numbers, the function returns a list of lists of products of the numbers in A and B. The lists must have the same dimensions.

Examples:
prod_(5, 3) returns 15.
prod_([1, 2, 3], 5) returns [5, 10, 15].
prod_([[1, 2], [3, 4]], 5) returns [[5, 10], [15, 20]].
prod_([1, 2, 3], [4, 5, 6]) returns [4, 10, 18].
prod_([[1, 2], [3, 4]], [[5, 6], [7, 8]]) returns [[5, 12], [21, 32]].
"""

def prod_(A, B):
    # START CODE HERE
    # END CODE HERE
    return AB_prod


from test_cases import test_prod_

test_prod_(prod_)
