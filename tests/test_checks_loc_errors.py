import numpy as np
import ie_pandas as ko

'''
This test passes GREEN
The test aims to veriry the correct implementation of the .loc functionality.
'''


def test_checks_loc_errors_simple():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }

    df = ko.DataFrame(my_dict)

    assert np.array_equal(df.loc(0), np.array([1, 2, 3]))
    assert df.loc(0, 0) == 1
    assert df.loc(3, 2)

    # Test to check that it catches bad column parameter
    try:
        df.loc(1.1)
        caught_error_1 = False
    except TypeError:
        caught_error_1 = True
    finally:
        assert caught_error_1

    # Test to check that it catches bad index parameter
    try:
        df.loc('int', 1.1)
        caught_error_2 = False
    except TypeError:
        caught_error_2 = True
    finally:
        assert caught_error_2

    # Test to check that it catches bad column with index
    try:
        df.loc(2.23, 1.1)
        caught_error_3 = False
    except TypeError:
        caught_error_3 = True
    finally:
        assert caught_error_3

    # Test to check that it catches bad column with good index
    try:
        df.loc(2.2, 1)
        caught_error_4 = False
    except TypeError:
        caught_error_4 = True
    finally:
        assert caught_error_4
