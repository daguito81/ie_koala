import numpy as np
import ie_koala as ko

'''
This test passes GREEN
'''


def test_simple_dataframe_index_column():
    my_dict = {
        'int': [1, 2, 3],
        'float': [1.1, 2.2, 3.3],
        'str': ['one', 'two', 'three'],
        'bool': [True, False, True]
    }
    df = ko.Dataframe(data=my_dict)

    expected_index = np.array([0, 1, 2])
    expected_columns = ['int', 'float', 'str', 'bool']

    assert np.array_equal(df.index, expected_index)
    assert np.array_equal(df.columns, expected_columns)
