"""
Function name: initialize_parameters

This function initializes the weights and biases of a neural network.

Arguments:
- input_layer_size: an integer, the number of input features.
- hidden_layer_size: an integer, the number of hidden units.
- output_layer_size: an integer, the number of output units.

Returns:
A dictionary containing the initialized weights and biases:
- W1: a list of lists of pseudo-normal values of shape (hidden_layer_size, input_layer_size).
- b1: a list of zeros of shape (hidden_layer_size, 1).
- W2: a list of lists of pseudo-normal values of shape (output_layer_size, hidden_layer_size).
- b2: a list of zeros of shape (output_layer_size, 1).

Example:
initialize_parameters(2, 4, 1) returns a dictionary:
{
    "W1": [[-0.001, 0.002], [0.003, -0.004], [-0.005, 0.006], [0.007, -0.008]],
    "b1": [[0], [0], [0], [0]],
    "W2": [[-0.009, 0.010, -0.011, 0.012]],
    "b2": [[0]]
}

Hint:
You can use the pseudo_norm_value() function to generate pseudo-normal values.
    Multiply the pseudo-normal values by 0.01 to scale them down and improve the learning.
    You can use the prod_() function to multiply a list of lists of numbers by a scalar.
You can use the zeros_() function to generate a list of zeros.
"""

def initialize_parameters(input_layer_size, hidden_layer_size, output_layer_size):
    # START CODE HERE
    # END CODE HERE
    return parameters


from test_cases import test_initialize_parameters

test_initialize_parameters(initialize_parameters)
