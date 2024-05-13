"""
Function name: sigmoid_

This function computes the sigmoid function of a number, or a list of numbers, or a list of lists of numbers.

Sigmoid function: https://en.wikipedia.org/wiki/Sigmoid_function
The sigmoid function of a number is defined as:
sigmoid(x) = 1 / (1 + e^(-x))

Arguments:
- X: a number, or a list of numbers, or a list of lists of numbers.

Returns:
- If X is a number, the function returns the sigmoid of X.
- If X is a list of numbers, the function returns a list of sigmoids of the numbers in X.
- If X is a list of lists of numbers, the function returns a list of lists of sigmoids of the numbers in X.

Examples:
sigmoid_(5) returns the sigmoid of 5.
sigmoid_([1, 2, 3]) returns a list of sigmoids of 1, 2, and 3.
sigmoid_([[1, 2], [3, 4]]) returns a list of lists of sigmoids of 1, 2, 3, and 4.

Hint:
You can use the math.exp() function to compute the exponential of a number.
```
from math import exp
value = exp(5)
```
"""

def sigmoid_(X):
    # START CODE HERE
    # END CODE HERE
    return value_or_list


from test_cases import test_sigmoid_

test_sigmoid_(sigmoid_)
