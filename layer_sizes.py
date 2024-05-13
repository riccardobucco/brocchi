"""
Function name: layer_sizes

This function computes the size of the input layer, the size of the hidden layer, and the size of the output layer for a neural network.

Arguments:
- X: the input dataset of shape (input size, number of examples)
- Y: the labels of shape (output size, number of examples)

Returns:
A tuple containing three integers:
- the size of the input layer
- the size of the hidden layer (which is fixed to 4)
- the size of the output layer
"""

def layer_sizes(X, Y):
    # START CODE HERE
    # END CODE HERE
    return input_layer_size, hidden_layer_size, output_layer_size


from test_cases import test_layer_sizes

test_layer_sizes(layer_sizes)
