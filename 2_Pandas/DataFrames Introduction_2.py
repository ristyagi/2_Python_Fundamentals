#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 19:00:46 2024

@author: Rishabh_Tyagi
"""

import pandas as pd
pd.set_option('display.max_columns', None)


# 02-------------------------------------------------------
# Differences between Shared Methods

rev = pd.read_csv('pandas/Complete/revenue.csv')
rev
rev.info()

rev = pd.read_csv('pandas/Complete/revenue.csv',index_col='Date') # setting one of the column from csv as index
rev

s = pd.Series([1,2,3])
s.sum() # sum method on series adds up all the series values

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



# 03-------------------------------------------------------
# Select one column from a Dataframe
# https://m.udemy.com/course/data-analysis-with-pandas/learn/lecture/40702696#overview

nba.head()
nba.info()

# pandas makes names of each column as attribute of dataframe and hence we can call that column name by simply using df.column_name. This is case sensitive. This works only when column name do not have space in it.
nba.Name
nba.Salary

nba['Team']
nba['Salary']
# this gives a view of original dataframe and not a copy of it.
# if we change or mutate this series then it will change in the original DF also.

names = nba['Name']
names.iloc[0] = 'Whateves' # here we are making change to name variable but that change is going to happen on the original DF. That is why we have a warning here.
names.head()

nba['Name']


# to avoid this, we should use .copy method instead of directly using the df column in other variables
nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas/nba.csv')
nba

names = nba['Name'].copy()
names
names.iloc[0] = 'Whatevs' # we made change to first value of Names
names.head()
nba['Name'] # but that change is not affecting the original dataframe


# 04-------------------------------------------------------
# Selecting multiple columns from a Dataframe
# https://m.udemy.com/course/data-analysis-with-pandas/learn/lecture/40702700#overview

nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas/nba.csv')
nba.info()

new_df = nba[['Salary','Name', 'Team']] # provide multiple column names as a list
new_df
new_df.info()
# this method gives a copy of original df and mutation on it will not change anything in original DF
# order here matters as new df will have columns in this order only
# instead of giving columns in selection syntax we can pass a list of column names too.

columns_to_select = ['Team','Name', 'Salary']
new_df2 = nba[columns_to_select]
new_df2
new_df2.info()




# 05-------------------------------------------------------
# Adding new column to DataFrame
# https://m.udemy.com/course/data-analysis-with-pandas/learn/lecture/40702704#overview

nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas/nba.csv')
nba
nba.info()

nba['Sport'] = 'Basketball' # we provided single static value, it will be added to each row of new column
nba['Sport']

# same as rows columns also conatain a index starting from 0.
# we can provide the index where we want to place our new column in insert method, it will shift rest of the columns right
nba.insert(loc=3, column = 'Sport', value = 'Basketball')
nba.info()
nba['Sport']

# usually we do not insert a single static value we take any existing column perform some operation on it and then add it as a new column
nba['Salary']
nba['Salary'] * 2 # this is called broadcasting as we can perform operation on df columns
nba['Salary'].mul(2) # using multiply method on df column and multiplying by 2
# both these ways gives new series with twice the original value but they are not yet inserted in df

nba['Salary Doubled'] = nba['Salary'] * 2
nba.info()
nba['Salary Doubled']

select_cols = ['Salary', 'Salary Doubled']
nba[select_cols]


nba['Salary'] - 5000000
# or
nba['Salary'].sub(5000000)
nba['New Salary'] = nba['Salary'].sub(5000000)
nba['New Salary']


new_sal = nba['Salary'].sub(1000) # first assigning new values to a variable
nba.insert(loc = 5, column = 'New Sal2', value = new_sal)# providing new col name and values to insert method
nba['New Sal2']
select_cols = ['Salary', 'Salary Doubled', 'New Sal2']
nba[select_cols]


#05-------------------------------------------------------
# Review of value_counts method

nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas/nba.csv')
nba.head()
nba.info()

# Value counts method coutns the number of times a unique value occurs in a col

nba['Team']
nba['Team'].value_counts()

nba['Position'].value_counts()
nba['Position'].value_counts(normalize=True) * 100 # this gives the percentages each value is part of the total values
nba['Salary'].value_counts()


check_cols = ['Team', 'Position']
nba[check_cols].value_counts() # how is this working?


#06-------------------------------------------------------
# Drop DataFrame rows with missing values

nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas/nba.csv')
nba.head()
nba.tail()
# nba.info()

nba.dropna() # outputs only 364 rows
# dropna has by default how = 'any' mean it will drop rows even it any of the column is Nan, we can change it to 'all' to drop only when all the columns are Nan
nba.dropna(how='all') # outputs 457 rows
nba.dropna(subset='College') # drop any row where college has Nan value

cols_to_check = ['College', 'Team']
nba.dropna(subset = cols_to_check) # dropping rows where college or team has Nan/missing values, it check for any one of them, not both of them


#07-------------------------------------------------------
# Fill in missing valeus with fillna method

nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas/nba.csv')
nba.head()
nba.tail()
nba.info()

nba.fillna(0) # this will insert 0 ata all the NaN occurances even in string fields, also this gives a new df and hence to be  assigned to a variable. This is not a good soltn as it will place random zeros at each missing data place.
nba['College']

nba['Salary'] # this will give the df column as a view and if we mutate it, it will make changes to the original df column. but if we call fillna() on it then it will return a copy.

nba['Salary'].fillna(0) # this is copy now and do not mutate the original df col
nba['Salary'] # check

nba['Salary'] = nba['Salary'].fillna(0)
nba['Salary'] # check , Nan values are updated to new 0.0 value
nba


nba['College'] = nba['College'].fillna(value = 'Unknown') # updating a string column's missing values
nba


#08-------------------------------------------------------
# As type method I

import pandas as pd
nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas_new/Complete/nba.csv')
nba.head()
nba.tail()
nba.info()

# astype method converts a column datatype to another data type
# even if the original dataset contains integers in a column, when it has some missing values pandas automatically reads it as floating
nba.dtypes

nba['Salary'].astype('int') # failing because pandas will not allow the conversion unless all NaN are handeled.

nba['Salary'] = nba['Salary'].fillna(0)
nba['Salary'] = nba['Salary'].astype('int')
nba.dtypes # salary column is not converted into int type from float

nba['Weight'] = nba['Weight'].fillna(0)
nba['Weight'] = nba['Weight'].astype('int')
nba.dtypes # weight column converted to int


#09-------------------------------------------------------
# As type method II

nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas_new/Complete/nba.csv').dropna(how='all')
nba.tail()

nba['Team'].nunique() # tells the number of unique values in that series
nba.nunique() # displays number of unique values in each column
nba.info()

# nba['Position'] = 
nba['Position'].nunique()
nba.info()

# such columns where unique values are small in a large dataset can be converted to special datatype called category. This uses memory consumption
nba['Position'] = nba['Position'].astype('category') # memory reduced from 36 to 33kb

nba['Team'] = nba['Team'].astype('string') # memory reduced to 30kb now
nba.info()


#10-------------------------------------------------------
# As sort_values I
nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas_new/Complete/nba.csv').dropna(how='all')
nba.tail()
nba.info()

# for dataframe we can use sort_values() method and need to pass a argument
# this will give a new df
# default order is ascending = True

rt = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/02_Sample_datasets/1_RT_sample_data.csv')
rt.head()
rt.info()


nba.sort_values('Name')
nba.sort_values(by = 'Name')
nba.sort_values(by = 'Name', ascending = False)

nba.sort_values(by = 'Salary', ascending = False)
# when there are missing values in a column, it sorts all the rows that have values and then puts all the rows where NaN is there in the end.
# we can pass argument for another parameter called na_position, default is last, and it will define where to place the rows where data is missing.

nba.sort_values(by = 'Salary')
nba.sort_values(by = 'Salary', na_position = 'first')

nba['Salary'].sort_values(ascending = False) # method chaining
nba['Salary'].sort_values(ascending = False, na_position = 'first') # method chaining


#11-------------------------------------------------------
# As sort_values II
nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas_new/Complete/nba.csv').dropna(how='all')
# nba.head()
nba.tail()
nba.info()


# we can provide a list of column names to by, which will then sort values by multiple columns

sort_order = ['Team', 'Name']
nba.sort_values(by = sort_order)
nba.sort_values(by = sort_order, na_position = 'first')

nba.sort_values(by = ['Team', 'Name'])
nba.sort_values(by = ['Team', 'Name'], ascending = True) # ascending order for both col
nba.sort_values(by = ['Team', 'Name'], ascending = False) # descending order for both col

nba.sort_values(by = ['Team', 'Name'], ascending = [True, False]) # ascending order for one and descending for another, lenght of order list should be same as the column list

nba = nba.sort_values(by = ['Team', 'Name'], ascending = [True, False]) # now original df is mutated
nba


#12-------------------------------------------------------
# Sort dataframe with sort_index()
nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas_new/Complete/nba.csv').dropna(how='all')
# nba.head()
nba.tail()
nba.info()


nba = nba.sort_values(['Team', 'Name'])
nba.head()

nba.sort_index() # default sort index in ascending order
nba.sort_index(ascending = False)
nba = nba.sort_index(ascending = False)
nba
# sc = pd.read_csv('/Users/Rishabh_Tyagi/Downloads/59_12_Feb24_Zone_SC_extract_All_depts.csv', verbose = True)

# sc = pd.read_csv('/Users/Rishabh_Tyagi/Downloads/59_12_Feb24_Zone_SC_extract_All_depts.csv')
sc.head()
sc.info()

#13-------------------------------------------------------
# Rank method
nba = pd.read_csv('/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/01. python_from_scratch/pandas_new/Complete/nba.csv').dropna(how='all')
# nba.head()
nba.tail()
nba.info()

nba['Salary']
nba['Salary'] = nba['Salary'].fillna(0).astype(int) # replacing missing values with 0 then converting series to int type

nba['Salary'].rank() # assigns rank 1 to smallest
nba['Salary'].rank(ascending = False) # assigns rank 1 to highest
nba['Salary'].rank(ascending = False).astype(int) # rank as whole number

nba['Salary_Rank'] = nba['Salary'].rank(ascending = False).astype(int)
nba.info()
nba

nba[['Name','Salary','Salary_Rank']].sort_values('Salary_Rank') # select columns with rank

nba.sort_values('Salary', ascending = False).head(10) # this gives a sort of Dense_rank() results
