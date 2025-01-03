## This Python cheat sheet is used as a go-to guide for frequently used piece of codes
## by - ristyagi@gmail.com


import pandas as pd
pd.set_option('display.max_columns', None)  # pandas setting to force terminal to display all columns of dataframe
pd.set_option('display.max_rows', None)  # pandas setting to force terminal to display all rows of dataframe

## ATTRIBUTE is a piece of data that belongs to the object, it simply stores a data/characteristic about the object, like df.shape,df.index,df.values, these store some info about dataframe
## METHOD on the other hand is a command or a behaviour that we ask the the object to perform for us.Like Head() method
## ARGUMENT is the value that we pass to a method
## PARAMETER 

## a FUNCTION is a set of instructions that can be used repeatedly
## while a METHOD is a function that is associated with an object

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


# we can provide the index where we want to place our new column in insert method, it will shift rest of the columns right
nba.insert(loc=3, column = 'Sport', value = 'Basketball')


# Value counts method coutns the number of times a unique value occurs in a col
nba['Team']
nba['Team'].value_counts()
nba['Position'].value_counts(normalize=True) * 100 # this gives the percentages each value is part of the total values


# Filtering data in dataframe 

pd.to_datetime(emp['Start Date'], format = '%m/%d/%Y') # format here is the format of existing date, so that pandas do no confuse month with day while converting.

pd.to_datetime(emp['Last Login Time'], format = '%H:%M %p') # since explicit date was not there, pandas automatically added default date, %p is used to specify am/pm value

pd.to_datetime(emp['Last Login Time'], format = '%H:%M %p').dt.time # dt.time object gives time component only

emp['Senior Management'] = emp['Senior Management'].astype('bool') # this converted NaN values as TRUE, which is not right

emp['Gender'] = emp['Gender'].astype('category') # this do not force change Nan to anything, keeps them as NaN

# directly reading csv and parse dates
emp = pd.read_csv("pandas/Complete/employees.csv", parse_dates = ['Start Date'], date_format = '%m/%d/%Y')

emp[emp['Gender'] == 'Male'] # this will pull out only those df rows where gender is Male


filter_cndtn = emp['Team'] == 'Finance' # make filter condition and pass it to df
emp[filter_cndtn]

emp[emp['Salary'] > 11000] ## all emp having salary > 110k

emp[emp['Start Date'] == '1996-03-31']

# How to get those rows from df where value of col in NaN

import datetime as dt

emp[emp['Last Login Time'] < dt.time(12, 0, 0)] # all emo who logged in before noon, compared only time column with time value only

is_female = emp['Gender'] == 'Female'
is_in_marketing = emp['Team'] == 'Marketing'

emp[is_female & is_in_marketing] # filtering with two conditions

emp[(emp['First Name'] == 'Douglas') & (emp['Salary'] == 97308)] # filter with two cndtns

emp[((emp['First Name'] == 'Douglas') 
    | (emp['First Name'] == 'Thomas'))
    & (emp['Gender'] == 'Male')]

name_cdtn = emp['First Name'] == 'Douglas'
name_cdtn2 = emp['First Name'] == 'Thomas'
gender_cndtn = emp['Gender'] == 'Male'

emp[name_cdtn | name_cdtn2 & gender_cndtn]
emp[(name_cdtn2 & gender_cndtn) | name_cdtn]

emp[emp['Team'].isin(['Finance', 'Product', 'Sales'])]
# or
fil = emp['Team'].isin(['Finance', 'Product', 'Sales'])
emp[fil]

# not in 
emp[~emp['Team'].isin(['Finance', 'Product', 'Sales'])]
# or
fil = ~emp['Team'].isin(['Finance', 'Product', 'Sales'])
emp[fil]

emp[emp['Team'].isnull()] # 43 rows where team is null as results
emp[emp['Team'].notnull()]
# or
emp[~emp['Team'].isnull()]
emp[~emp['Team'].notnull()] # 43 rows where team is null as results

# col1 null and col2 null
emp[emp['First Name'].isnull() & emp['Team'].isnull()]
