import ie_pandas as ko

'''
This test passes GREEN
This test aims to verify that a TypeError is raised
if the data passed in the DataFrame function is not in the right format (dictionary).
'''


def test_checks_data_dict_simple():

    try:
        _ = ko.DataFrame(data=[1, 2, 3, 4, 5])
        error_catched = 0
    except TypeError:
        error_catched = 1

    assert error_catched == 1
