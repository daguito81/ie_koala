import numpy as np
import ie_koala as ko
import pytest

'''
This test is RED
the index functionality is not yet implemented
'''


@pytest.mark.parametrize("col, expected_output", [
    ('int', np.array([1, 2, 3])),
    ('float', np.array([1.1, 2.2, 3.3])),
    ('str', np.array(['one', 'two', 'three'])),
    ('bool', np.array([True, False, True])),
])
def test_df_indexing_col(col, expected_output):
    my_dict = {
        'int': [1, 2, 3],
        'float': [1.1, 2.2, 3.3],
        'str': ['one', 'two', 'three'],
        'bool': [True, False, True]
    }
    df = ko.Dataframe(data=my_dict)

    result = df.loc(col)

    assert np.array_equal(result, expected_output)


@pytest.mark.parametrize("col, row, expected_output", [
    ('int', 0, np.array(1)),
    ('float', 1, np.array(2.2)),
    ('str', 2, np.array('three')),
    ('bool', 3, np.array(False)),
])
def test_df_indexing_col_ind(col, row, expected_output):
    my_dict = {
        'int': [1, 2, 3, 4],
        'float': [1.1, 2.2, 3.3, 4.4],
        'str': ['one', 'two', 'three', 'four'],
        'bool': [True, False, True, False]
    }
    df = ko.Dataframe(data=my_dict)

    result = df.loc(col, row)

    assert np.array_equal(result, expected_output)
