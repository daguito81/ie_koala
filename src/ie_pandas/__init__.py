import numpy as np
import itertools as it


class DataFrame:
    """
    Creates a DataFrame Object to interact with the data

    In this section, the basic functionalities of the DataFrame class are created.
    
    The arguments of the function are:

    Parameters
    ---------------
    data : dict
        Must be a dictionary of lists or dictionary of numpy arrays.
        All the elements of the dictionary must have the same length.
    columns=None : list of strings
        Must be a list of strings.
        The number of items in the list must be the same size as the number
        of keys in the dictionary passed to the data.
    index=None : list of integers
        Must be a list of integers.
        This attribute is not currently in use for any functionality.
        get_row() works with the index being 0 - indexed at all times.

    Example:
    ---------------
    from ie_pandas import DataFrame
    my_dict = {
        'int': [1, 2, 3],
        'float': [1.1, 2.2, 3.3],
        'string': ['one', 'two', 'three'],
    }
    df = DataFrame(data=my_dict, columns=['integer', 'float', 'strings'], index=[0, 1, 2])

    Visualizing:
    The DataFrame can be visualized by simply passing the name in an interactive shell
    or by calling the print(df) function.

    """

    def __init__(self, data, columns=None, index=None):

        # This checks if the provided data is a dictionary
        if type(data) != dict:
            raise TypeError("Data needs to be a dictionary")
        elif type(data[list(data)[0]]) != list \
                and type(data[list(data)[0]]) != np.ndarray:
            raise TypeError("Dictionary needs to be of lists or numpy arrays")
        else:
            self.data = data.values()  # Dict values as attribute

        # This checks that all arrays inside the dict are the same length
        test = []
        for i in self.data:
            test.append(len(i))
        if len(set(test)) != 1:
            raise ValueError("Lenght of all arrays must be equal")

        # Constructor if no columns parameter is passed
        if columns is None:
            self.columns = []  # To keep column names as list of strings
            for col in list(data):
                self.columns.append(str(col))

            # Constructor if no index is provided
            if index is None:
                self.index = np.arange(len(data[list(data)[0]]))

            # Constructor if index is provided
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

        # Constructor if column parameter is passed
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
                        # This index is not used so far but set for future
        # This creates the "meat" of the dataframe object
        self.df = dict(zip(self.columns, self.data))
        # This casts the data into np.arrays in case they were lists
        for key in self.df:
            self.df[key] = np.array(self.df[key])

    def _frame(self):
        """
        Arguments:

        Returns:
            A formatted version of the dataframe. 

        Similar to:

        """
        matrix = zip(*[list(value) if isinstance(list(value), list)
                       else it.repeat(list(value))
                       for key, value in self.df.items()])
        title = ''.join(['{:15}'.format(key) for key in self.df.keys()])
        dtypes = ''.join(['{:15}'.format(str(self.df[key].dtype))
                          for key in self.df.keys()])
        spacer = ""
        data = ""
        for row in matrix:
            data = data +\
                 ''.join(['{:15}'.format(str(item)) for item in row]) +\
                 "\n"

        table = title + "\n" + dtypes + "\n" + spacer + "\n" + data
        return table

    # This is to give instructions on how to print the dataframe
    def __repr__(self):
        return self._frame()

    # Prints the DataFrame as well
    def __str__(self):
        return self._frame()

    # This allows bracket indexing " df["colname"] "
    def __getitem__(self, item):
        return np.array(self.df[item])

    # This allows the DataFrame to be updated with new data
    # This can replace or add columns
    # Only works with full columns
    def __setitem__(self, idx, newcol):
        if type(newcol) != np.ndarray:
            raise TypeError("Input needs to be a numpy array")
        if len(newcol) != len(self.df[self.columns[0]]):
            raise ValueError("Input needs to be same length as dataframe")
        self.df[idx] = newcol
        self.columns = list(self.df)

    # This function returns the length of a specific column
    def __len__(self):
        """
        Docstring here

        Arguments: 
        
        
        Returns:
            The length of a specific column in the dataframe.

        Similar to: 
            len() function in pandas
        """
        return len(self.df[list(self.df)[0]])

    # This function allows us to index by columns and rows
    # in string or integers df.loc(0, 0) <- returns the top left element
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
            elif type(col) == str:
                return np.array(self.df[col][row])
            else:
                raise TypeError("Column needs to be Integer or String")

    # This returns a list of all the column elements in a row
    def get_row(self, row):
        if type(row) != int:
            raise TypeError("Row needs to be an Integer")
        result = []
        for col in self.df.keys():
            result.append(self[col][row])
        return result

    # These are all aggregation functions (they return a list)
    def sum(self):
        """
        Arguments:
        
        Results:

        Similar to:
        """
        result = []
        for key in self.df.keys():
            if (np.issubdtype(type(self.df[key][0]), np.number))\
                    or (type(self.df[key][0]) == np.bool_):
                result.append(self.df[key].sum())
        return result

    def min(self):
        """
        Arguments:

        Results:

        Similar to:
        """
        result = []
        for key in self.df.keys():
            if (np.issubdtype(type(self.df[key][0]), np.number))\
                    or (type(self.df[key][0]) == np.bool_):
                result.append(self.df[key].min())
        return result

    def max(self):
        """
        Arguments:

        Results:

        Similar to:
        """
        result = []
        for key in self.df.keys():
            if (np.issubdtype(type(self.df[key][0]), np.number))\
                    or (type(self.df[key][0]) == np.bool_):
                result.append(self.df[key].max())
        return result

    def mean(self):
        """
        Arguments:

        Results:

        Similar to:

        """
        result = []
        for key in self.df.keys():
            if (np.issubdtype(type(self.df[key][0]), np.number))\
                    or (type(self.df[key][0]) == np.bool_):
                result.append(self.df[key].mean())
        return result

    def median(self):
        """
        Arguments:

        Results:

        Similar to:
        """
        result = []
        for key in self.df.keys():
            if (np.issubdtype(type(self.df[key][0]), np.number))\
                    or (type(self.df[key][0]) == np.bool_):
                result.append(np.median(self.df[key]))
        return result

    def std(self):
        """
        Arguments:

        Results:

        Similar to:
        """
        result = []
        for key in self.df.keys():
            if (np.issubdtype(type(self.df[key][0]), np.number))\
                    or (type(self.df[key][0]) == np.bool_):
                result.append(self.df[key].std())
        return result

    def rename(self, old_col, new_col, inplace=True):
        """
        Renames a column in the DataFrame. 

        Arguments:
            old_col: string
                current name of the column
            new_col: string 
                new name of the column
            inplace: boolean
                This parameter defines if the change will be done to the current
                instance of the DataFrame or return a new instance with the new attributes.
                The old_col must be inside a DataFrame.

        """
        if type(new_col) != str or type(old_col) != str:
            raise TypeError("Column name needs to be a String")
        if type(inplace) != bool:
            raise TypeError("Inplace can only be Boolean")
        if old_col not in self.columns:
            raise ValueError("{} is not in the Dataframe".format(old_col))

        new_dict = {}
        for key, value in zip(self.df.keys(), self.df.values()):
            new_key = key if key != old_col else new_col
            new_dict[new_key] = self.df[key]
        if inplace:
            self.df = new_dict
            self.columns = list(self.df)
        else:
            return DataFrame(new_dict)

    def drop(self, drop_col, inplace=True):
        """
        Drops the specified column from a DataFrame.

        Arguments:
        drop_col: string
            the column to be dropped from the DataFrame
            must be a string and present in the DataFrame
        inplace: boolean
            Defines if the change will be done to the current
            instance of the Dataframe or return a new instance with the new attributes.
            
        """
        if type(drop_col) != str:
            raise TypeError("Column name needs to be a string")
        if type(inplace) != bool:
            raise TypeError("Inplace can only be Boolean")
        if drop_col not in self.columns:
            raise ValueError("This column is not in DataFrame")

        if inplace:
            self.df.pop(drop_col)
            self.columns = list(self.df)
        else:
            df_copy = self.df.copy()
            df_copy.pop(drop_col)
            return DataFrame(df_copy)
