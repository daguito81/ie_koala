import numpy as np
import ie_pandas as ko

"""
This test is RED
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
        'newcol': np.array(['a', 'b', 'c', 'd', 'e'])
    }

    df = ko.DataFrame(data=my_dict)

    df['int'] = np.array([20, 21, 22, 23, 24])
    df['newcol'] = np.array(['a', 'b', 'c', 'd', 'e'])

    assert df.df == new_dict
