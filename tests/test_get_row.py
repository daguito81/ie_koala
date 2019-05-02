import numpy as np
import ie_pandas as ko

"""
This test passes GREEN
"""


def test_get_row():
    my_dict = {
        "int": np.array([1, 2, 3, 4, 5]),
        "float": np.array([1.1, 2.2, 3.3, 4.4, 5.5]),
        "str": np.array(["one", "two", "three", "four", "five"]),
        "bool": np.array([True, False, True, False, True]),
        4: np.array([1, 2, 3, 4, 5]),
        True: np.array([6, 7, 8, 9, 10]),
    }

    df = ko.DataFrame(data=my_dict)

    expected_row1 = [1, 2, 3, 4, 5]
    expected_row2 = [1.1, 2.2, 3.3, 4.4, 5.5]
    expected_row3 = "one", "two", "three", "four", "five"]
    expected_row4 = [True, False, True, False, True]
    expected_row5 = [1, 2, 3, 4, 5]
    expected_row6 = True: np.array([6, 7, 8, 9, 10]

    assert np.array_equal(df.get_row(0), expected_row1)
    assert np.array_equal(df.get_row(1), expected_row2)
    assert np.array_equal(df.get_row(2), expected_row3)
    assert np.array_equal(df.get_row(3), expected_row4)
    assert np.array_equal(df.get_row(4), expected_row5)
    assert np.array_equal(df.get_row(5), expected_row6)
