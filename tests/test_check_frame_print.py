import ie_pandas as pd

'''
This test passes GREEN
This test aims to verify that the pretty print function works
As it uses the .frame() function, adn returns a string object called
table which when printed it shows as as a table"
'''


def test_checks_frame_print_simple():
    my_dict = {
        'int': [1, 2, 3],
        'float': [1.1, 2.2, 3.3],
        'string': ['one', 'two', 'three'],
    }

    df = pd.DataFrame(my_dict)

    expected_result = 'int            float          string         \n'\
        'int32          float64        <U5            \n'\
        '\n'\
        '1              1.1            one            \n'\
        '2              2.2            two            \n'\
        '3              3.3            three          \n'

    assert df.frame() == expected_result
