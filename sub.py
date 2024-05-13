"""
Function name: sub_

This function computes the difference between two numbers, or two lists of numbers, or a number and a list of numbers, or a number and a list of lists of numbers, or two lists of lists of numbers.

Matrix addition: https://en.wikipedia.org/wiki/Matrix_addition
Matrix addition is the operation of adding two matrices by adding the corresponding entries together.

Arguments:
- A: a number, or a list of numbers, or a list of lists of numbers.
- B: a number, or a list of numbers, or a list of lists of numbers.

Returns:
- If A and B are numbers, the function returns the difference between A and B.
- If A is a number and B is a list of numbers, the function returns a list of differences between A and the numbers in B.
- If A is a list of numbers and B is a number, the function returns a list of differences between the numbers in A and B.
- If A is a number and B is a list of lists of numbers, the function returns a list of lists of differences between A and the numbers in B.
- If A is a list of lists of numbers and B is a number, the function returns a list of lists of differences between the numbers in A and B.
- If A and B are lists of numbers, the function returns a list of differences between the numbers in A and B. The lists must have the same length.
- If A and B are lists of lists of numbers, the function returns a list of lists of differences between the numbers in A and B. The lists must have the same dimensions.

Examples:
sub_(5, 3) returns 2.
sub_([1, 2, 3], 5) returns [-4, -3, -2].
sub_(5, [1, 2, 3]) returns [4, 3, 2].
sub_([[1, 2], [3, 4]], 5) returns [[-4, -3], [-2, -1]].
sub_(5, [[1, 2], [3, 4]]) returns [[4, 3], [2, 1]].
sub_([1, 2, 3], [4, 7, 9]) returns [-3, -5, -6].
sub_([[1, 2], [3, 4]], [[1, 5], [3, 2]]) returns [[0, -3], [0, 2]].

Hint:
You can use the neg_() function to compute the negation of a number, or a list of numbers, or a list of lists of numbers.
And you can use the add_() function to compute the sum of two numbers, or two lists of numbers, or a number and a list of numbers, or a number and a list of lists of numbers, or two lists of lists of numbers.
"""

def sub_(A, B):
    # START CODE HERE
    # END CODE HERE
    return AB_sub


from test_cases import test_sub_

test_sub_(sub_)
