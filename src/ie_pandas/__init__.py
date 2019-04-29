import numpy as np
import itertools as it


class DataFrame:
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
                    elif type(index[0]) != int:
                        raise TypeError(
                            "index needs to be in integers"
                        )
                    else:
                        self.index = np.array(index)
        else:
            if type(columns) != list:
                raise TypeError("column parameter needs to be a list")

            self.columns = []  # To keep column names as list of strings
            for col in columns:
                self.columns.append(col)

            if len(self.columns) != len(data.values()):
                raise ValueError("List of column names need to be "
                                 "equal to number of columns")

            if index is None:
                self.index = np.arange(len(data[list(data)[0]]))

            else:
                if len(index) != len(data[list(data)[0]]):
                    raise ValueError("Length mismatch: data != index")
                else:
                    if type(index) != list:
                        raise TypeError(
                            "index parameter needs to be a list")
                    elif type(index[0]) != int:
                        raise TypeError(
                            "index needs to be in integers"
                        )
                    else:
                        self.index = np.array(index)
                        # removed the index from being part of the dict
        self.df = dict(zip(self.columns, self.data))
        # This is a copy of the Dataframe

    @property  # This is some voodoo to make it print like a table
    def frame(self):
        """
        Docstring here
        This is to pretty print the dataframe
        """
        frame = self.df
        self._frame = frame
        matrix = zip(*[list(value) if isinstance(list(value), list)
                       else it.repeat(list(value))
                       for key, value in frame.items()])
        print(''.join(['{:15}'.format(key) for key in frame.keys()]))
        for row in matrix:
            print(''.join(['{:15}'.format(str(item)) for item in row]))

    def __repr__(self):
        return "Koala Dataframe, use .frame to visualize or print(df)"

    def __str__(self):
        return f"{self.df}"

    def __getitem__(self, item):
        return np.array(self.df[item])

    def loc(self, col, row=None):
        if row is None:
            if type(col) == int:
                return np.array(self.df[list(self.df)[col]])
            elif type(col) == str:
                return np.array(self.df[col])
            else:
                raise TypeError("Column needs to be Integer or String")
        else:
            if type(row) != int:
                raise TypeError("Index needs to be Integer")
            if type(col) == int:
                return np.array(self.df[list(self.df)[col]][row])
            elif type(col == str):
                return np.array(self.df[col][row])
            else:
                raise TypeError("Column needs to be Integer or String")
