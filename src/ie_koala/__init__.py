import numpy as np
import itertools as it


class Dataframe:
    """
    Dataframe docstring
    #TODO Fill this
    """

    def __init__(self, data, columns=None, index=None):

        if type(data) != dict:
            raise TypeError("Data needs to be a dictionary")
        else:
            self.data = data.values()  # Dict values as attribute

        if columns is None:
            self.columns = []  # To keep column names as list of strings
            for col in list(data):
                self.columns.append(str(col))

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
                self.columns = []  # To keep column names as list of strings
                for col in columns:
                    self.columns.append(col)

                if len(self.columns) != len(data.values()):
                    raise ValueError("List of column names need to be "
                                     "equal to number of columns")
                else:
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
                        self.index = np.array(index)
                        # removed the index from being part of the dict

    @property  # This is some voodoo to make it print like a table
    def frame(self):
        frame = dict(zip(self.columns, self.data))
        self._frame = frame
        matrix = zip(*[value if isinstance(value, list) else it.repeat(value)
                       for key, value in frame.items()])
        print(''.join(['{:15}'.format(key) for key in frame.keys()]))
        for row in matrix:
            print(''.join(['{:15}'.format(str(item)) for item in row]))

    def __repr__(self):
        return "Koala Dataframe, use .frame to visualize or print(df)"

    def __str__(self):
        return f"{dict(zip(self.columns, self.data))}"

# Removed the notes as I put them as issues on the repo
