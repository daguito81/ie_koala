import numpy as np
import ie_pandas as ko

'''
This test passes GREEN
'''


def test_checks_data_dict_simple():
    good_dict_ls = {
        'int': [1, 2, 3],
        'float': [1.1, 2.2, 3.3],
    }
    good_dict_np = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
    }
    bad_dict = {
        'int': "Hello",
        'float': "World",
    }
    # Test that everything works with lists
    df = ko.DataFrame(good_dict_ls)
    assert np.array_equal(df['int'], np.array([1, 2, 3]))
    # Test that everything works with np.ndarrays
    df = ko.DataFrame(good_dict_np)
    assert np.array_equal(df['int'], np.array([1, 2, 3]))

    # Check the error handling for Bug #43
    try:
        ko.DataFrame(bad_dict)
        error_catched = 0
    except TypeError:
        error_catched = 1

    assert error_catched == 1
