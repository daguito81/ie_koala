import numpy as np
import ie_pandas as ko

"""
This test is GREEN
These are the tests to validate functioning of updating & adding columns of a dataframe. 
"""


def test_set_items():
    my_dict = {
        "int": np.array([1, 2, 3, 4, 5]),
        "float": np.array([1.1, 2.2, 3.3, 4.4, 5.5]),
        "str": np.array(["one", "two", "three", "four", "five"]),
        "bool": np.array([True, False, True, False, True]),
        4: np.array([1, 2, 3, 4, 5]),
        True: np.array([6, 7, 8, 9, 10]),
    }
    new_dict = {
        "int": np.array([20, 21, 22, 23, 24]),
        "float": np.array([1.1, 2.2, 3.3, 4.4, 5.5]),
        "str": np.array(["one", "two", "three", "four", "five"]),
        "bool": np.array([True, False, True, False, True]),
        4: np.array([1, 2, 3, 4, 5]),
        True: np.array([6, 7, 8, 9, 10]),
        "newcol": np.array(['a', 'b', 'c', 'd', 'e']),
        "newcol2": np.array([10, 11, 12, 13, 14]),
    }

    df = ko.DataFrame(data=my_dict)
    new_df = ko.DataFrame(data=new_dict)

    df['int'] = np.array([20, 21, 22, 23, 24])
    df['newcol'] = np.array(['a', 'b', 'c', 'd', 'e'])
    df['newcol2'] = np.array([10, 11, 12, 13, 14])

    # This is to check that the column was updated
    assert (df['int'] == new_df['int']).all()
    # This is to check that a non existant column was added
    assert (df['newcol'] == new_df['newcol']).all()
    # This is to make sure that df.columns was updated
    assert (df.columns == new_df.columns)
    # This is to check that all the items are the same
    for i in range(len(df.columns)):
        assert (df[df.columns[i]] == new_df[df.columns[i]]).all()
