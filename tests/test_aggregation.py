import numpy as np
import ie_pandas as ko

"""
This test passes GREEN
"""


def test_aggregation():
    my_dict = {
        "int": np.array([1, 2, 3, 4, 5]),
        "float": np.array([1.1, 2.2, 3.3, 4.4, 5.5]),
        "str": np.array(["one", "two", "three", "four", "five"]),
        "bool": np.array([True, False, True, False, True]),
        4: np.array([1, 2, 3, 4, 5]),
        True: np.array([6, 7, 8, 9, 10]),
    }

    df = ko.DataFrame(data=my_dict)

    expected_sum = [15, 16.5, 3, 15, 40]
    expected_min = [1, 1.1, False, 1, 6]
    expected_max = [5, 5.5, True, 5, 10]
    expected_mean = [3.0, 3.3, 0.6, 3.0, 8.0]
    expected_median = [3.0, 3.3, 1.0, 3.0, 8.0]
    expected_std = [
        1.4142135623730951,
        1.5556349186104046,
        0.48989794855663565,
        1.4142135623730951,
        1.4142135623730951,
    ]

    assert np.array_equal(df.sum(), expected_sum)
    assert np.array_equal(df.min(), expected_min)
    assert np.array_equal(df.max(), expected_max)
    assert np.array_equal(df.mean(), expected_mean)
    assert np.array_equal(df.median(), expected_median)
    assert np.array_equal(df.std(), expected_std)
