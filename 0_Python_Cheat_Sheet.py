## This Python cheat sheet is used as a go-to guide for frequently used piece of codes
## by - ristyagi@gmail.com

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


# setting one of the column from csv as index
rev = pd.read_csv('pandas/Complete/revenue.csv',index_col='Date')


rev.sum() # in df sum() method sums up all the values of each column
rev.sum(axis=0) #sum across vertical axis for all columns, returns a series, this is same as sum()
# or use
rev.sum(axis='index')

rev.sum(axis=1) #sum across horizontal axis for all columns, returns a series
# or use
rev.sum(axis='columns')

# sum of all the values of df
rev.sum().sum() # this is called method chaining
rev.sum(axis=1).sum()


nba['Name'].iloc[0] # accessing index 0 element of a df column

names = nba['Name'].copy() # getting a separate copy of names column in a new series

names.iloc[0] = 'Whatevs' # setting 0 index value of series to some new value

new_df = nba[['Salary','Name', 'Team']] # provide multiple column names as a list to get all columns from a df in a new df
# or
columns_to_select = ['Team','Name', 'Salary']
new_df2 = nba[columns_to_select]


