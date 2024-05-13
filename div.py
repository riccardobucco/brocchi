"""
Function name: div_

This function computes the division of two numbers, or two lists of numbers, or a number and a list of numbers, or a number and a list of lists of numbers, or two lists of lists of numbers.

Arguments:
- A: a number, or a list of numbers, or a list of lists of numbers.
- B: a number, or a list of numbers, or a list of lists of numbers.

Returns:
- If A and B are numbers, the function returns the division of A by B.
- If A is a number and B is a list of numbers, the function returns a list of divisions of A by the numbers in B.
- If A is a list of numbers and B is a number, the function returns a list of divisions of the numbers in A by B.
- If A is a number and B is a list of lists of numbers, the function returns a list of lists of divisions of A by the numbers in B.
- If A is a list of lists of numbers and B is a number, the function returns a list of lists of divisions of the numbers in A by B.
- If A and B are lists of numbers, the function returns a list of divisions of the numbers in A by B. The lists must have the same length.
- If A and B are lists of lists of numbers, the function returns a list of lists of divisions of the numbers in A by B. The lists must have the same dimensions.

Examples:
div_(5, 2) returns 5 / 2 (which is 2.5).
div_([1, 2, 3], 5) returns [0.2, 0.4, 0.6].
div_(5, [1, 2, 4]) returns [5, 2.5, 12.5].
div_([[1, 2], [3, 4]], 2) returns [[0.5, 1], [1.5, 2]].
div_(5, [[1, 2], [5, 4]]) returns [[5, 2.5], [1, 1.25]].
div_([1, 2, 3], [4, 2, 1]) returns [0.25, 1, 3].
div_([[1, 2], [3, 4]], [[1, 2], [6, 2]]) returns [[1, 1], [0.5, 2]].
"""

def div_(A, B):
    # START CODE HERE
    # END CODE HERE
    return AB_div


from test_cases import test_div_

test_div_(div_)
