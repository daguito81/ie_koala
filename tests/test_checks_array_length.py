import numpy as np
import ie_pandas as ko

'''
This test passes GREEN
This test aims to verify that the DataFrame function in ie_pandas provides
an error message if the length of the columns is not the same
for the whole data frame
'''


def test_length_check_simple():
    my_dict_bad = {
        'int': np.array([1, 2, 3, 4]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }
    try:
        ko.DataFrame(data=my_dict_bad)
        error_catched = 0
    except ValueError:
        error_catched = 1

    assert error_catched == 1
