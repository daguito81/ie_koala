import ie_pandas as ko

'''
This test passes GREEN
The test aims to verify the corret implementation of the repr functionality.
'''


def test_checks_repr_simple():
    my_dict = {
        'int': [1, 2, 3],
        'float': [1.1, 2.2, 3.3],
        'string': ['one', 'two', 'three'],
    }

    expected_result = 'int            float          string         \n'\
        'int32          float64        <U5            \n'\
        '\n'\
        '1              1.1            one            \n'\
        '2              2.2            two            \n'\
        '3              3.3            three          \n'

    df = ko.DataFrame(my_dict)

    assert df.__repr__() == expected_result
