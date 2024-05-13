"""
Function name: sum_matrix

This function computes the sum of all elements in a matrix, or the sum of elements along a specified axis.

Arguments:
- X: a list of lists of numbers.
- axis: an integer, the axis along which the sum is computed.
    If axis is None, the function computes the sum of all elements in the matrix X.
    If axis is 0, the function computes the sum of elements in each column.
    If axis is 1, the function computes the sum of elements in each row.

Returns:
- If axis is None, the function returns the sum of all elements in the matrix X.
- If axis is 0, the function returns a list of sums of elements in each column.
- If axis is 1, the function returns a list of sums of elements in each row.

Examples:
sum_matrix([[1, 2], [3, 4], [5, 6]]) returns [[21]].
sum_matrix([[1, 2], [3, 4], [5, 6]], axis=0) returns [[9, 12]].
sum_matrix([[1, 2], [3, 4], [5, 6]], axis=1) returns [[3], [7], [11]].

Note:
The axes which are reduced are left in the result as dimensions with size one
"""

def sum_matrix(X, axis=None):
    # START CODE HERE
    # END CODE HERE
    return sums


from test_cases import test_sum_matrix

test_sum_matrix(sum_matrix)
