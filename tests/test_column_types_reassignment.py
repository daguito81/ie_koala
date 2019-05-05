import ie_pandas as ko
import numpy as np
import pytest
'''
This test is GREEN
The purpose of this is to validate correct reassignment of data types
inside an existing dataframe.
'''


@pytest.mark.parametrize("col_index, col_name, col_result, name_type", [
    (0, 'int', 'integer', str),
    (1, 'float', 'floating', str),
    (2, 'str', 'string', str),
    (3, 'bool', 'boolean', str),
    (4, '4', 'four', str),
])
def test_column_names_types_reassignment(col_index,
                                         col_name,
                                         col_result,
                                         name_type):
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
        4: np.array([1, 2, 3]),
    }

    df = ko.DataFrame(my_dict)

    assert df.columns == ['int', 'float', 'str', 'bool', '4']

    assert df.columns[col_index] == col_name

    df.columns[col_index] = col_result
    assert df.columns[col_index] == col_result
    assert type(df.columns[col_index]) == name_type
