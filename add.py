"""
Function name: add_

This function computes the sum of two numbers, or two lists of numbers, or a number and a list of numbers, or a number and a list of lists of numbers, or two lists of lists of numbers.
The function should return the same result if the order of the arguments is swapped,
i.e. add_(A, B) should return the same result as add_(B, A) (the function is commutative).

Matrix addition: https://en.wikipedia.org/wiki/Matrix_addition
Matrix addition is the operation of adding two matrices by adding the corresponding entries together.

Arguments:
- A: a number, or a list of numbers, or a list of lists of numbers.
- B: a number, or a list of numbers, or a list of lists of numbers.

Returns:
- If A and B are numbers, the function returns the sum of A and B.
- If A is a number and B is a list of numbers, the function returns a list of sums of A and the numbers in B.
- If A is a list of lists of numbers and B is number, the function returns a list of lists of sums of the numbers in A and B.
- If A and B are lists of numbers, the function returns a list of sums of the numbers in A and B. The lists must have the same length.
- If A and B are lists of lists of numbers, the function returns a list of lists of sums of the numbers in A and B. The lists must have the same dimensions.

Examples:
sum_(5, 3) returns 8.
sum_([1, 2, 3], 5) returns [6, 7, 8].
sum_([[1, 2], [3, 4]], 5) returns [[6, 7], [8, 9]].
sum_([1, 2, 3], [4, 5, 6]) returns [5, 7, 9].
sum_([[1, 2], [3, 4]], [[5, 6], [7, 8]]) returns [[6, 8], [10, 12]].
"""

def add_(A, B):
    # START CODE HERE
    # END CODE HERE
    return AB_sum


from test_cases import test_add_

test_add_(add_)
