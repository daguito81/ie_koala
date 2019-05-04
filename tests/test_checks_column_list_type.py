import numpy as np
import ie_pandas as ko

'''
This test passes ???
'''


def test_checks_column_list_type_simple():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }
    try:
        _ = ko.DataFrame(data=my_dict, columns=[1, 2, 3, 4])  # Good
        _ = ko.DataFrame(data=my_dict, columns="One Two Three Four")  # Bad
        error_catched = 0
    except TypeError:
        error_catched = 1

    assert error_catched == 1
