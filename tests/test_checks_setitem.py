import numpy as np
import ie_pandas as ko

'''
This test passes GREEN
This test aims to verify that a TypeError is raised
if the type of the new column is not a np.ndarray and that a
ValueError is raised if the length of the new column is not equal
 to the length of the old column.
'''


def test_checks_set_item_errors_simple():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }

    df = ko.DataFrame(my_dict)

    try:
        df['int'] = [1, 2, 3]
        caught_error_1 = 0
    except TypeError:
        caught_error_1 = 1

    try:
        df['int'] = np.array([1, 2, 3, 4, 5])
        caught_error_2 = 0
    except ValueError:
        caught_error_2 = 1

    assert caught_error_1 == 1
    assert caught_error_2 == 1
