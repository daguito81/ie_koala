import numpy as np
import ie_pandas as ko

'''
This test passes GREEN
The test aims to verify the corret implementation of the repr functionality.
'''


def test_checks_repr_simple():
    my_dict = {
        'int': np.array([1, 2, 3]),
        'float': np.array([1.1, 2.2, 3.3]),
        'str': np.array(['one', 'two', 'three']),
        'bool': np.array([True, False, True]),
    }

    df = ko.DataFrame(my_dict)

    assert \
        df.__repr__() == "Koala Dataframe, use" \
        " .frame to visualize or print(df)"
