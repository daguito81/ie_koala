import numpy as np
import ie_pandas as ko

'''
This test passes GREEN
It checks whether the assignment as string works properly.
'''


def test_checks_str_simple():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }

    dict_str = "{"\
        "'int': array([1, 2, 3]), "\
        "'float': array([1.1, 2.2, 3.3]), "\
        "'str': array(['one', 'two', 'three'], dtype='<U5'), "\
        "'bool': array([ True, False,  True])"\
        "}"

    df = ko.DataFrame(my_dict)

    assert df.__str__() == dict_str
