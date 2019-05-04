import ie_pandas as ko
import numpy as np
import pytest
'''
This test is GREEN
'''


@pytest.mark.parametrize("old_col, new_col, col_result", [
    ('int', 'integer', ['integer', 'float', 'str', 'bool', '4']),
    ('float', 'floating', ['int', 'floating', 'str', 'bool', '4']),
    ('str', 'string', ['int', 'float', 'string', 'bool', '4']),
    ('bool', 'boolean', ['int', 'float', 'str', 'boolean', '4']),
    ('4', 'four', ['int', 'float', 'str', 'bool', 'four']),
])
def test_column_rename(old_col, new_col, col_result):
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
        4: np.array([1, 2, 3]),
    }

    df = ko.DataFrame(my_dict)
    original_columns = ['int', 'float', 'str', 'bool', '4']
    # This is to make sure constructor works fine
    assert df.columns == original_columns

    # Make the checks for inplace=False
    df2 = df.rename(old_col, new_col, inplace=False)
    for col in df2.columns:  # To make sure they are all strings
        assert type(col) == str

    assert list(df2.df) == col_result  # Chgeck keys in self.df
    assert df2.columns == col_result  # Check expected results
    assert df.columns == original_columns  # Check df was not modified

    df.rename(old_col, new_col, inplace=True)  # Rename Method here
    for col in df.columns:  # To make sure they are all strings
        assert type(col) == str

    assert list(df.df) == col_result  # Chgeck keys in self.df
    assert df.columns == col_result  # Check expected results


@pytest.mark.parametrize("drop_col, col_result", [
    ('int', ['float', 'str', 'bool', '4']),
    ('float', ['int', 'str', 'bool', '4']),
    ('str', ['int', 'float', 'bool', '4']),
    ('bool', ['int', 'float', 'str', '4']),
    ('4', ['int', 'float', 'str', 'bool']),
])
def test_column_drop(drop_col, col_result):
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
        4: np.array([1, 2, 3]),
    }

    df = ko.DataFrame(my_dict)
    original_columns = ['int', 'float', 'str', 'bool', '4']
    # This is to make sure constructor works fine
    assert df.columns == original_columns

    df2 = df.drop(drop_col, inplace=False)  # Rename Method here
    for col in df2.columns:  # To make sure they are all strings
        assert type(col) == str
    assert list(df2.df) == col_result  # Chgeck keys in self.df
    assert df2.columns == col_result  # Check expected results
    assert df.columns == original_columns

    df.drop(drop_col, inplace=True)  # Rename Method here
    for col in df.columns:  # To make sure they are all strings
        assert type(col) == str
    assert df.columns == col_result  # Check expected results


def test_col_rename_errors():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
        4: np.array([1, 2, 3]),
    }

    df = ko.DataFrame(my_dict)

    # Test that new col is a string
    try:
        df.rename('int', 3, inplace=True)
        caught_error_1 = False
    except TypeError:
        caught_error_1 = True
    finally:
        assert caught_error_1

    # Test that old col is a string
    try:
        df.rename(3, 'int', inplace=True)
        caught_error_2 = False
    except TypeError:
        caught_error_2 = True
    finally:
        assert caught_error_2

    # Test that inplace is Boolean
    try:
        df.rename('int', 3, inplace="Seven")
        caught_error_3 = False
    except TypeError:
        caught_error_3 = True
    finally:
        assert caught_error_3

    # Test that old_col is in the DataFrame
    try:
        df.rename('hello', 'goodbye', inplace=True)
        caught_error_4 = False
    except ValueError:
        caught_error_4 = True
    finally:
        assert caught_error_4


def test_col_drop_errors():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
        4: np.array([1, 2, 3]),
    }

    df = ko.DataFrame(my_dict)

    # Test that the drop_col is an string
    try:
        df.drop(3, inplace=True)
        caught_error_1 = False
    except TypeError:
        caught_error_1 = True
    finally:
        assert caught_error_1

    # Test that the inplace is Boolean
    try:
        df.drop('int', inplace="Seven")
        caught_error_2 = False
    except TypeError:
        caught_error_2 = True
    finally:
        assert caught_error_2
    # Test that the drop_col is part of the DataFrame
    try:
        df.drop('hello', inplace=True)
        caught_error_3 = False
    except ValueError:
        caught_error_3 = True
    finally:
        assert caught_error_3
