import pandas as pd
pd.set_option('display.max_columns', None)  # pandas setting to force terminal to display all columns of dataframe
pd.set_option('display.max_rows', None)  # pandas setting to force terminal to display all rows of dataframe

## ATTRIBUTE is a piece of data that belongs to the object, it simply stores a data/characteristic about the object, like df.shape,df.index,df.values, these store some info about dataframe
## METHOD on the other hand is a command or a behaviour that we ask the the object to perform for us.Like Head() method
## ARGUMENT is the value that we pass to a method
## PARAMETER 

df.info()
df.describe()
df.columns  # gives all the headers of dataframe columns as a index object
df.shape
df.index  # gives range of index of a dataframe
df.values  # this gives the data of dataframe in a numpy array object
df.dtypes  # gives a series with column names of df as index and series values as datatypes of the columns


# DICT to DataFrame
import pandas as pd
import numpy as np
base_data = {
    'area' : [2600,3000,3200,3600,4000],
    'bedrooms' : [3,4,np.nan,3,5],
    'age' : [20,15,18,30,8],
    'price' : [550000,565000,610000,595000,760000]
    }
df = pd.DataFrame(base_data)

