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
# https://udemy.com/course/data-analysis-with-pandas/learn/lecture/40702696#overview

nba.head()
nba.info()

# pandas makes names of each column as attribute of dataframe and hence we can call that column name by simply using df.column_name. This is case sensitive. This works only when column name do not have space in it.
nba.Name
nba.Salary

nba['Team']
nba['Salary']
# this gives a view of original dataframe and not a copy of it.
# if we change or mutate this series then it will change in the original DF also.

nba['Name'].iloc[0] # accessing index 0 element of column

names = nba['Name']
names.iloc[0]
names.iloc[0] = 'Whateves' # here we are making change to name variable but that change is going to happen on the original DF. That is why we have a warning here.
names.head()

nba['Name']


# to avoid this, we should use .copy method instead of directly using the df column in other variables
nba = pd.read_csv("pandas/Complete/nba.csv") 
nba

names = nba['Name'].copy() # getting a separate copy of names column in a new series
names
names.iloc[0] = 'Whatevs' # we made change to first value of Names
names.head()
nba['Name'] # but that change is not affecting the original dataframe



# 04-------------------------------------------------------
# Selecting multiple columns from a Dataframe
# https://udemy.com/course/data-analysis-with-pandas/learn/lecture/40702700#overview

nba = pd.read_csv("pandas/Complete/nba.csv") 
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

new_df2['Name'].iloc[0]

new_df2['Name'].iloc[0] = 'Whatever'

new_df2['Name'].iloc[0]

nba['Name'].iloc[0] # since original df's index0 name is not changed that proves that new_df2 was copy of original df
