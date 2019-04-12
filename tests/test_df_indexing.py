import numpy as np
import ie_koala as ko
import pytest


@pytest.mark.parametrize("col, expected_output", [
    ('int', np.array([1, 2, 3])),
    ('float', np.array([1.1, 2.2, 3.3])),
    ('str', np.array(['one', 'two', 'three'])),
    ('bool', np.array([True, False, True])),
])
def test_df_indexing(col, expected_output):
    my_dict = {
        'int': [1, 2, 3],
        'float': [1.1, 2.2, 3.3],
        'str': ['one', 'two', 'three'],
        'bool': [True, False, True]
    }
    df = ko.Dataframe(data=my_dict)

    result = df.index(col)

    assert np.array_equal(result, expected_output)
