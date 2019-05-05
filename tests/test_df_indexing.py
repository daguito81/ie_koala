import numpy as np
import ie_pandas as ko
import pytest

'''
This test is GREEN
Purpose of the test is to check the functioning of
indexing inside a dataframe, by column.
It checks for the indexing by a string or an integer
based on name or position of the column.
'''


@pytest.mark.parametrize("col, expected_output", [
    ('int', np.array([1, 2, 3])),
    ('float', np.array([1.1, 2.2, 3.3])),
    ('str', np.array(['one', 'two', 'three'])),
    ('bool', np.array([True, False, True])),
])
def test_df_indexing_col(col, expected_output):
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }
    df = ko.DataFrame(data=my_dict)

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
        'int': np.array([1, 2, 3, 4]),
        'float': np.array([1.1, 2.2, 3.3, 4.4]),
        'str': np.array(['one', 'two', 'three', 'four']),
        'bool': np.array([True, False, True, False]),
    }
    df = ko.DataFrame(data=my_dict)

    result = df.loc(col, row)

    assert np.array_equal(result, expected_output)


# Test added to test indexing of columns by number (Bug #19)
@pytest.mark.parametrize("col, row, expected_output", [
    (0, 0, np.array(1)),
    (1, 1, np.array(2.2)),
    (2, 2, np.array('three')),
    (3, 3, np.array(False)),
])
def test_df_indexing_col_int_ind(col, row, expected_output):
    my_dict = {
        'int': np.array([1, 2, 3, 4]),
        'float': np.array([1.1, 2.2, 3.3, 4.4]),
        'str': np.array(['one', 'two', 'three', 'four']),
        'bool': np.array([True, False, True, False]),
    }
    df = ko.DataFrame(data=my_dict)

    result = df.loc(col, row)

    assert np.array_equal(result, expected_output)


# Test added to test indexing of columns by number (Bug #19)
@pytest.mark.parametrize("col, row, expected_output", [
    ('int', 0, np.array(1)),
    ('float', 1, np.array(2.2)),
    ('str', 2, np.array('three')),
    ('bool', 3, np.array(False)),
])
def test_df_indexing_bracket_col_int_ind(col, row, expected_output):
    my_dict = {
        'int': np.array([1, 2, 3, 4]),
        'float': np.array([1.1, 2.2, 3.3, 4.4]),
        'str': np.array(['one', 'two', 'three', 'four']),
        'bool': np.array([True, False, True, False]),
    }
    df = ko.DataFrame(data=my_dict)

    result = df[col][row]

    assert np.array_equal(result, expected_output)
