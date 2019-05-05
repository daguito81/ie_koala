import numpy as np
import ie_pandas as ko

"""
This test passes GREEN
Test to validate consitent length of all arrays (columns) in a dataframe
"""


def test_len():
    my_dict = {
        "int": np.array([1, 2, 3, 4, 5]),
        "float": np.array([1.1, 2.2, 3.3, 4.4, 5.5]),
        "str": np.array(["one", "two", "three", "four", "five"]),
        "bool": np.array([True, False, True, False, True]),
        4: np.array([1, 2, 3, 4, 5]),
        True: np.array([6, 7, 8, 9, 10]),
    }

    df = ko.DataFrame(data=my_dict)

    expected_len = 5

    assert len(df) == expected_len
