# ie_pandas
## MBD 2018 - Adv.Python - Group K

Dagoberto Romer  
Meredith Hayward  
Andrea Salvati  
Moritz Steinbrecher

***

ie_pandas is a python library to deal with DataFrames. It suports the creation of a dataframe object from a dictionary of data. It supports mixed data types between its different columns, but can only hold 1 data type per column.

***
# Features
The current functionality of the library is:
1) Import data from a dictionary of Numpy arrays or dictionary of lists (int, float, bool an strings are supported)
2) String-based bracket indexing Ex: `df['sales']` that returs the respective column in a Numpy array.
3) String and integer based indexing using the `df.loc()` method Ex: df.loc(2,3) for doing 
4) Aggregation functions (sum, min, max, mean, median, std supported)
5) Modification and adding new columns by reassigning numpy arrays to indexed columns Ex: `df['int] = np.array(...)`
6) Column renaming and column drop both as copies and in place
7) print the data in both dictionary and table format by using `print(df)` for dictionary or `df.frame` for table output

The data is also treated as a dictionary inside the Object so we can access it with the `df` attribute and then make any operation to it that would be possible to do on a dictionary. Including passing it into another data library like pandas.

# Installation
## User installation:

To use the library, you must do these steps:  
1) `git clone https://github.com/daguito81/ie_koala.git`
2) `cd ie_koala`
3) `pip install .`

ie_pandas has numpy as a requirement and will be installed when installed throuhg pip.  

Take note that the folder is called ie_koala when imported, this is just to avoid confusion between similarly packaged libraries.  
For usage inside a python script, we need to import:  
* `import ie_pandas as pd`  
or  
* `from ie_pandas import DataFrame`  

For the sake of this documentation we will import the DataFrame class from the library. 

Example:  
```
import numpy as np
from ie_pandas import DataFrame

my_dict = {
    'int': [1, 2, 3],
    'float': [1.1, 2.2, 3.3],
    'str': ['one', 'two', 'three'],
    'bool': [True, False, True],
}

# Then we can create the DataFrame with
df = DataFrame(my_dict)
```
With the DataFrame created we can use aggregate it's columns by different functions
```
df.sum()  # To add all the elements of numeric columns
df.min()  # To find the minimum value of every numeric columns
df.max()  # To find the maximum value of every numeric column
df.mean()  # To find the mean of every numeric column
df.median()  # To find the median of every numeric column
df.std()  # To find the standard deviation fo every numeric columns
```
We can also index the columns by integers or strings using bracket indexing or integer indexing  
Examples:  
```
df['int']  # returns array([1, 2, 3])
df['float']  # returns array([1.1, 2.2, 3.3])
# We can also index by integer using the df.loc() notation
df.loc(0)  # Returns array([1, 2, 3])
df.loc(0, 1)  # Returns array(2) which is a scalar
# Note that df.loc() notation is (Column, Row)
```

We can also rename the columns:  
```
df.rename('int', 'integer', inplace=True)  # To change the current instance
df2 = df.rename('int', 'integer', inplace=False)  # To create a copy instead
```
Or drop a column:
```
df.drop('int', inplace=True)  # To drop it from the current instance
df2 = df.drop('int', inplace=Flase)  # To create a copy instead
```
We can also replace a column by bracket indexing and assigning the new column:
```
df['int'] = np.array([10, 11, 12])
# Note that the new column needs to be passed as a numpy array
# Note that the length needs to be the same as the length of the rest of the dataframe
```
We can also add a new column by simply assigning it a new column name
```
df['newcol'] = np.array(['New', 'Data', 'Here'])
# Note that the same restrictions as updating a columns exist
```
### Visualize
To visualize the dataframe, we have provided 2 methods.  
1) to view it as a dictionary you can use `print(df)`
2) to see it as a table you must use `df.frame`

# Developer Instructions
To contribute and develop on the ie_pandas library, any issue or feature needs to be tested and be fully 100% pep8 compliant. We use flake8 for styling and unit testing to test the code in the library.  

## Installation
To install the library for development purposes do :
1) `git clone https://github.com/daguito81/ie_koala.git`
2) `cd ie_koala`
3) `pip install -e .[dev]`

This will allow the library to dynamically include the changes to the code without having to reinstall the package after every change.  
The[dev] parameter will allow it to include the extra packages for testing.  
In case of any trouble running the tests. You can manually install them with:  
```
pip install pytest
pip install pytest-cov
pip install pytest-flake8
```

## Testing
All new tests should be included in the tests folder.

To check that tests pass run in the ie_koala directory:  
`pytest --cov=ie_pandas tests/`  
This will check all the tests and the code coverage of said tests.
We aim to have 90%+ code coverage in our tests.  

To test for style errors we can run:  
`pytest --flake8`  
And this will show all errors that don't conform with flake8 which include pep8

To run only the tests just use in ie_koala folder:  
`pytest`

In case there is an error installing. To run the tests, install on the same environment as ie-pandas:  
`pip install pytest-cov`  
`pip install pytest-flake8`