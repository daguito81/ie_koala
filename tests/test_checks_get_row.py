import numpy as np
import ie_pandas as ko

'''
This test passes GREEN
This test aims to verify that get_row function returns the expected row
and that it raises a TypeError if an invalid argument is passed in it.
'''


def test_checks_get_row_errors_simple():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }

    df = ko.DataFrame(my_dict)

    assert df.get_row(0) == [1, 1.1, 'one', True]

    try:
        df.get_row('a')
        caught_error_1 = False
    except TypeError:
        caught_error_1 = True

    assert caught_error_1
