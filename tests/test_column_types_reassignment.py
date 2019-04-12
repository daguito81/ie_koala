import ie_koala as ko
import pytest
'''
This test pases 100% GREEN
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
        'int': [1, 2, 3],
        'float': [1.1, 2.2, 3.3],
        'str': ['one', 'two', 'three'],
        'bool': [True, False, True],
        4: [1, 2, 3],
        }

    df = ko.Dataframe(my_dict)

    assert df.columns == ['int', 'float', 'str', 'bool', '4']

    assert df.columns[col_index] == col_name

    df.columns[col_index] = col_result
    assert df.columns[col_index] == col_result
    assert type(df.columns[col_index]) == name_type
