from itertools import chain
from statistics import mean, variance


def test_layer_sizes(f):
    assert f([[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) == (2, 4, 5)
    assert f([[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]) == (2, 4, 2)
    assert f([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == (3, 4, 3)

def test_pseudo_norm_value(f):
    vals = [f() for _ in range(10000)]
    assert abs(mean(vals)) < 0.05
    assert abs(variance(vals) - 1) < 0.05
    vals = f(5)
    assert isinstance(vals, list)
    assert len(vals) == 5
    assert all(isinstance(val, float) for val in vals)
    vals = f(5, 3)
    assert isinstance(vals, list)
    assert len(vals) == 5
    assert all(isinstance(val, list) for val in vals)
    assert all(len(val) == 3 for val in vals)
    assert all(isinstance(val, float) for sublist in vals for val in sublist)

def test_zeros_(f):
    assert f() == 0
    assert f(5) == [0, 0, 0, 0, 0]
    assert f(2, 3) == [[0, 0, 0], [0, 0, 0]]

def test_log_(f):
    log_05 = -0.69314
    log_4 = 1.38629
    log_1 = 0
    assert f(0.5) - log_05 < 0.00001
    vals = f([0.5, 4])
    assert isinstance(vals, list)
    assert len(vals) == 2
    for val, expected in zip(vals, [log_05, log_4]):
        assert val - expected < 0.00001
    vals = f([[0.5, 4], [1, 4], [1, 1]])
    assert isinstance(vals, list)
    assert len(vals) == 3
    for lst, expected_lst in zip(vals, [[log_05, log_4], [log_1, log_4], [log_1, log_1]]):
        assert isinstance(lst, list)
        assert len(lst) == 2
        for val, expected in zip(lst, expected_lst):
            assert val - expected < 0.00001

def test_tanh_(f):
    tanh_05 = 0.46211
    tanh_4 = 0.99933
    tanh_1 = 0.76159
    assert f(0.5) - tanh_05 < 0.00001
    vals = f([0.5, 4])
    assert isinstance(vals, list)
    assert len(vals) == 2
    for val, expected in zip(vals, [tanh_05, tanh_4]):
        assert val - expected < 0.00001
    vals = f([[0.5, 4], [1, 4], [1, 1]])
    assert isinstance(vals, list)
    assert len(vals) == 3
    for lst, expected_lst in zip(vals, [[tanh_05, tanh_4], [tanh_1, tanh_4], [tanh_1, tanh_1]]):
        assert isinstance(lst, list)
        assert len(lst) == 2
        for val, expected in zip(lst, expected_lst):
            assert val - expected < 0.00001

def test_sigmoid_(f):
    sigmoid_05 = 0.62246
    sigmoid_4 = 0.98201
    sigmoid_1 = 0.73106
    assert f(0.5) - sigmoid_05 < 0.00001
    vals = f([0.5, 4])
    assert isinstance(vals, list)
    assert len(vals) == 2
    for val, expected in zip(vals, [sigmoid_05, sigmoid_4]):
        assert val - expected < 0.00001
    vals = f([[0.5, 4], [1, 4], [1, 1]])
    assert isinstance(vals, list)
    assert len(vals) == 3
    for lst, expected_lst in zip(vals, [[sigmoid_05, sigmoid_4], [sigmoid_1, sigmoid_4], [sigmoid_1, sigmoid_1]]):
        assert isinstance(lst, list)
        assert len(lst) == 2
        for val, expected in zip(lst, expected_lst):
            assert val - expected < 0.00001

def test_abs_(f):
    assert f(5) == 5
    assert f([-1, 2, -3]) == [1, 2, 3]
    assert f([[1, -2], [3, -4]]) == [[1, 2], [3, 4]]

def test_neg_(f):
    assert f(5) == -5
    assert f([5, 3]) == [-5, -3]
    assert f([[5, 3], [1, 4], [1, 1]]) == [[-5, -3], [-1, -4], [-1, -1]]

def test_inv_(f):
    assert f(5) == 0.2
    assert f([5, 2]) == [0.2, 0.5]
    assert f([[5, 2], [1, 4], [1, 1]]) == [[0.2, 0.5], [1, 0.25], [1, 1]]

def test_add_(f):
    assert f(5, 3) == 8
    assert f([1, 2, 3], 5) == [6, 7, 8]
    assert f([[1, 2], [3, 4]], 5) == [[6, 7], [8, 9]]
    assert f([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert f([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[6, 8], [10, 12]]
    assert f(3, 5) == 8
    assert f(5, [1, 2, 3]) == [6, 7, 8]
    assert f(5, [[1, 2], [3, 4]]) == [[6, 7], [8, 9]]
    assert f([4, 5, 6], [1, 2, 3]) == [5, 7, 9]
    assert f([[5, 6], [7, 8]], [[1, 2], [3, 4]]) == [[6, 8], [10, 12]]

def test_prod_(f):
    assert f(5, 3) == 15
    assert f([1, 2, 3], 5) == [5, 10, 15]
    assert f([[1, 2], [3, 4]], 5) == [[5, 10], [15, 20]]
    assert f([1, 2, 3], [4, 5, 6]) == [4, 10, 18]
    assert f([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[5, 12], [21, 32]]
    # Commutative tests
    assert f(3, 5) == 15
    assert f(5, [1, 2, 3]) == [5, 10, 15]
    assert f(5, [[1, 2], [3, 4]]) == [[5, 10], [15, 20]]
    assert f([4, 5, 6], [1, 2, 3]) == [4, 10, 18]
    assert f([[5, 6], [7, 8]], [[1, 2], [3, 4]]) == [[5, 12], [21, 32]]

def test_sub_(f):
    assert f(5, 3) == 2
    assert f([1, 2, 3], 5) == [-4, -3, -2]
    assert f(5, [1, 2, 3]) == [4, 3, 2]
    assert f([[1, 2], [3, 4]], 5) == [[-4, -3], [-2, -1]]
    assert f(5, [[1, 2], [3, 4]]) == [[4, 3], [2, 1]]
    assert f([1, 2, 3], [4, 7, 9]) == [-3, -5, -6]
    assert f([[1, 2], [3, 4]], [[1, 5], [3, 2]]) == [[0, -3], [0, 2]]

def test_div_(f):
    tests = [
        ((5, 2), 2.5),
        (([1, 2, 3], 5), [0.2, 0.4, 0.6]),
        ((5, [1, 2, 4]), [5, 2.5, 1.25]),
        (([[1, 2], [3, 4]], 2), [[0.5, 1], [1.5, 2]]),
        ((5, [[1, 2], [5, 4]]), [[5, 2.5], [1, 1.25]]),
        (([1, 2, 3], [4, 2, 1]), [0.25, 1, 3]),
        (([[1, 2], [3, 4]], [[1, 2], [6, 2]]), [[1, 1], [0.5, 2]]),
    ]
    for args, expected in tests:
        if isinstance(expected, list) and all(isinstance(val, (int, float)) for val in expected):
            for val, exp in zip(f(*args), expected):
                assert abs(val - exp) < 0.00001
        elif isinstance(expected, list) and all(isinstance(val, list) for val in expected):
            for lst, exp_lst in zip(f(*args), expected):
                for val, exp in zip(lst, exp_lst):
                    assert abs(val - exp) < 0.00001
        else:
            assert abs(f(*args) - expected) < 0.00001

def test_transpose_(f):
    assert f([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
    assert f([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

def test_matrix_mul(f):
    assert f([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
    assert f([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]) == [[58, 64], [139, 154]]

def test_sum_matrix(f):
    assert f([[1, 2], [3, 4], [5, 6]]) == [[21]]
    assert f([[1, 2], [3, 4], [5, 6]], axis=0) == [[9, 12]]
    assert f([[1, 2], [3, 4], [5, 6]], axis=1) == [[3], [7], [11]]

def test_initialize_parameters(f):
    n_x, n_h, n_y = 5, 4, 3
    params = f(n_x, n_h, n_y)
    assert 'W1' in params and 'b1' in params and 'W2' in params and 'b2' in params
    assert len(params['W1']) == n_h
    assert all(len(row) == n_x for row in params['W1'])
    assert len(params['b1']) == n_h
    assert all(len(row) == 1 for row in params['b1'])
    assert len(params['W2']) == n_y
    assert all(len(row) == n_h for row in params['W2'])
    assert len(params['b2']) == n_y
    assert all(len(row) == 1 for row in params['b2'])
    n_x, n_h, n_y = 500, 40, 30
    params = f(n_x, n_h, n_y)
    vals = list(chain(*params['W1']))
    assert abs(mean(vals)) < 0.0005
    assert 0.999 < abs(variance(vals) - 1) < 1
