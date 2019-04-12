import numpy as np


class Dataframe:
    """
    Dataframe docstring
    #TODO Fill this
    """

    def __init__(self, data, columns=None, index=None):

        if type(data) != dict:
            raise TypeError("Data needs to be a dictionary")

        if columns is None:
            self.columns = np.array(list(data), dtype=str)

            if index is None:
                self.index = np.arange(len(data[list(data)[0]]))

            else:
                if len(index) != len(data[list(data)[0]]):
                    raise ValueError("Length mismatch: data != index")
                else:
                    if type(index) != list:
                        raise TypeError(
                            "index parameter needs to be a list")
                    else:
                        self.index = np.array(index)
        else:
            if type(columns) != list:
                raise TypeError("column parameter needs to be a list")
            else:
                self.columns = np.array(columns, dtype=str)
                data = dict(zip(self.columns, data.values()))

            if index is None:
                self.index = np.arange(len(data[list(data)[0]]))

            else:
                if len(index) != len(data[list(data)[0]]):
                    raise ValueError("Length mismatch: data != index")
                else:
                    if type(index) != list:
                        raise TypeError(
                            "index parameter needs to be a list")
                    else:
                        data['index'] = np.array(index)
                        self.index = data['index']


'''
Notes:
1) We need to refactor the index and column creation as their own functions
so that we don't repeat code over again
2) we need to create tests for edge cases and handle errors
3) We need to make a check that all lists inside the data dictionary are of
 the same length
'''
