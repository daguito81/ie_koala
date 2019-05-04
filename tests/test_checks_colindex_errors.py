import numpy as np
import ie_pandas as ko

'''
This test passes GREEN
'''


def test_checks_emptycols_index_simple():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }

    # Test wrong index length
    try:
        df = ko.DataFrame(my_dict, index=[1, 2, 3, 4])
        caught_error_1 = False
    except ValueError:
        caught_error_1 = True

    # Test wrong index type
    try:
        df = ko.DataFrame(my_dict, index={1: 1, 2: 2, 3: 3})
        caught_error_2 = False
    except TypeError:
        caught_error_2 = True

    # Test wrong index member type
    try:
        df = ko.DataFrame(my_dict, index=["a", "b", "c"])
        caught_error_3 = False
    except TypeError:
        caught_error_3 = True

    assert caught_error_1 is True
    assert caught_error_2 is True
    assert caught_error_3 is True

    expected_index = np.array([1, 2, 3])

    df = ko.DataFrame(my_dict, index=[1, 2, 3])

    assert np.array_equal(df.index, expected_index)


def test_checks_fullcols_index_simple():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }

    # Test wrong index length
    try:
        df = ko.DataFrame(my_dict,
                          columns=['Integer', 'Float', 'String', 'Boolean'],
                          index=[1, 2, 3, 4])
        caught_error_1 = False
    except ValueError:
        caught_error_1 = True

    # Test wrong index type
    try:
        df = ko.DataFrame(my_dict,
                          columns=['Integer', 'Float', 'String', 'Boolean'],
                          index={1: 1, 2: 2, 3: 3})
        caught_error_2 = False
    except TypeError:
        caught_error_2 = True

    # Test wrong index member type
    try:
        df = ko.DataFrame(my_dict,
                          columns=['Integer', 'Float', 'String', 'Boolean'],
                          index=['a', 'b', 'c'])
        caught_error_3 = False
    except TypeError:
        caught_error_3 = True

    assert caught_error_1 is True
    assert caught_error_2 is True
    assert caught_error_3 is True

    expected_index = np.array([1, 2, 3])

    df = ko.DataFrame(my_dict,
                      columns=['Integer', 'Float', 'String', 'Boolean'],
                      index=[1, 2, 3])

    assert np.array_equal(df.index, expected_index)
