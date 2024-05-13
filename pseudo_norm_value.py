"""
Function name: pseudo_norm_value

This function generates pseudo-normal values using the Central Limit Theorem.

Central Limit Theorem: https://en.wikipedia.org/wiki/Central_limit_theorem
In simple words, suppose that a large sample of observations is obtained,
each observation being randomly produced in a way that does not depend on the values of the other observations,
and that the average (arithmetic mean) of the observed values is computed.
If this procedure is performed many times, resulting in a collection of observed averages,
the central limit theorem says that if the sample size was large enough,
the probability distribution of these averages will closely approximate a normal distribution.

Arguments:
- *args: a variable number of integers, representing the size of each dimension of the output list.

Returns:
- If no arguments are provided, the function returns a single pseudo-normal value.
- If one argument is provided, the function returns a list of pseudo-normal values of the specified size.
- If more than one argument is provided, the function returns a list of pseudo-normal values of the specified size in each dimension.

Examples:
pseudo_norm_value() returns a single pseudo-normal value.
pseudo_norm_value(5) returns a list of 5 pseudo-normal values.
pseudo_norm_value(2, 3) returns a list of 2 lists, each containing 3 pseudo-normal values.

How to generate a pseudo-normal value:
1. Generate a (possibly large) sample of random values.
    These numbers could be 0 or 1 with equal probability (expected value is 0.5, variance is 0.25).
    Or you can use any other distribution you prefer, for example numbers between 1 and 10 (expected value is 5.5, variance is 8.25).
2. Calculate  the "sample mean", i.e. the average of these values (which should be close to the expected value of the distribution).
    Formula: sample_mean = (x1 + x2 + ... + xn) / n
3. Calculate the "sample standard deviation", i.e. the standard deviation of these numbers
    Formula: sample_stdev = sqrt(expected variance) / sqrt(n)
3. Subtract the expected value from the "sample mean".
4. Divide the result by the "sample standard deviation".

Hint:
You can use the random.randint() function to generate random values.
It returns a random integer in range [a, b], including both end points.
```
from random import randint
value = randint(0, 1)
```
"""

def pseudo_norm_value(*args):
    # START CODE HERE
    # END CODE HERE
    return value_or_list


from test_cases import test_pseudo_norm_value

test_pseudo_norm_value(pseudo_norm_value)
