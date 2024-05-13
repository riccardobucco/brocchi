"""
Function name: log_

This function computes the natural logarithm of a number, or a list of numbers, or a list of lists of numbers.

Natural logarithm: https://en.wikipedia.org/wiki/Natural_logarithm
The natural logarithm of a number is the power to which the base (Euler's number) must be raised to obtain the number.

Arguments:
- X: a number, or a list of numbers, or a list of lists of numbers.

Returns:
- If X is a number, the function returns the natural logarithm of X.
- If X is a list of numbers, the function returns a list of natural logarithms of the numbers in X.
- If X is a list of lists of numbers, the function returns a list of lists of natural logarithms of the numbers in X.

Examples:
log_(5) returns the natural logarithm of 5.
log_([1, 2, 3]) returns a list of natural logarithms of 1, 2, and 3.
log_([[1, 2], [3, 4]]) returns a list of lists of natural logarithms of 1, 2, 3, and 4.

Hint:
You can use the math.log() function to compute the natural logarithm of a number.
```
from math import log
value = log(5)
```
"""

def log_(X):
    # START CODE HERE
    # END CODE HERE
    return value_or_list


from test_cases import test_log_

test_log_(log_)
