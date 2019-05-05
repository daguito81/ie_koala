import numpy as np
import ie_pandas as ko

"""
This test is GREEN
The test is to validate the functioning of horizontal indexing.
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

    expected_row0 = [1, 1.1, "one", True, 1, 6]
    expected_row1 = [2, 2.2, "two", False, 2, 7]
    expected_row2 = [3, 3.3, "three", True, 3, 8]
    expected_row3 = [4, 4.4, "four", False, 4, 9]
    expected_row4 = [5, 5.5, "five", True, 5, 10]

    assert df.get_row(0) == expected_row0
    assert df.get_row(1) == expected_row1
    assert df.get_row(2) == expected_row2
    assert df.get_row(3) == expected_row3
    assert df.get_row(4) == expected_row4
