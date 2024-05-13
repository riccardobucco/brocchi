"""
Function name: tanh_

This function computes the hyperbolic tangent of a number, or a list of numbers, or a list of lists of numbers.

Hyperbolic tangent: https://en.wikipedia.org/wiki/Hyperbolic_function
The hyperbolic tangent of a number is the ratio of the hyperbolic sine to the hyperbolic cosine.
The hyperbolic tangent of a number can be computed using the formula:
tanh(x) = 2 / (1 + e^(-2 * x)) - 1

Arguments:
- X: a number, or a list of numbers, or a list of lists of numbers.

Returns:
- If X is a number, the function returns the hyperbolic tangent of X.
- If X is a list of numbers, the function returns a list of hyperbolic tangents of the numbers in X.
- If X is a list of lists of numbers, the function returns a list of lists of hyperbolic tangents of the numbers in X.

Examples:
tanh_(5) returns the hyperbolic tangent of 5.
tanh_([1, 2, 3]) returns a list of hyperbolic tangents of 1, 2, and 3.
tanh_([[1, 2], [3, 4]]) returns a list of lists of hyperbolic tangents of 1, 2, 3, and 4.

Hint:
You can use the math.exp() function to compute the exponential of a number.
```
from math import exp
value = exp(5)
```
"""

def tanh_(X):
    # START CODE HERE
    # END CODE HERE
    return value_or_list


from test_cases import test_tanh_

test_tanh_(tanh_)
