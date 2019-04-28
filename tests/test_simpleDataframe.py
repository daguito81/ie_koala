import numpy as np
import ie_pandas as ko

'''
This test passes GREEN
'''


def test_simple_dataframe_index_column():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }
    df = ko.DataFrame(data=my_dict)

    expected_index = np.array([0, 1, 2])
    expected_columns = ['int', 'float', 'str', 'bool']

    assert np.array_equal(df.index, expected_index)
    assert np.array_equal(df.columns, expected_columns)
