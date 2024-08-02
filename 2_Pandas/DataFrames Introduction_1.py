#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 19:00:46 2024

@author: Rishabh_Tyagi
"""

import pandas as pd
pd.set_option('display.max_columns', None) # pandas setting to force terminal to display all columns of dataframe
# pd.set_option('display.max_rows', None) # pandas setting to force terminal to display all rows of dataframe

# Dataframe object is workhorse of pandas library and its just a 2-D table consisting of rows and columns
# Its a data structure consisting of rows and columns
# Its a collection of series that have been connected or stitched together with a common index.

nba = pd.read_csv("pandas/Complete/nba.csv") # read_csv defaults to read csv as a dataframe object
nba.shape
nba.info()
nba.describe()
nba.columns


# 01-------------------------------------------------------
# Shared attributes and methods between series and dataframes
# https://m.udemy.com/course/data-analysis-with-pandas/learn/lecture/40702688#overview

# since these are two diff data structures, there are some common attributes and methods, they may return different results in both cases because of different underlying data.

    ## Attribute is a piece of data that belongs to the object, it simply stores a data/characteristic about the object, like df.shape, its a tuple having info of dataframe shape
    ## method on the other hand is a command or a behaviour that we ask the the object to perform for us.Like Head() method

# essentially a dataframe object comprises of smaller different objects to make up this big object, like many series objects

s = pd.Series([1,2,3,4,5])
s

nba.head()  # same as series head gives a new dataframe
            # head() method has a default parameter n =5 with argument 5 and hence when no 
nba.head(1)
nba.tail(5) # tail does same but for bottom of dataframe
nba.tail(1)

# by default index values are numberical and start from zero
# but we can set any column values are index label explicitly

# index and values are attributes that are present for series and are also present for dataframes
# index gives is the underlying obeject that stores the index values or labesl
# values gives the underlying n-d numpy array that is stored by pandas
# n-d array is just an array of arrays

nba.index
nba.values  # this gives the data of dataframe in a numpy array object

s1 = [[1,2],[3,4]] # this is a list of lists
s1

nba.shape # shape attribute gives the number of rows followed by number of columns.

nba.dtypes # gives a series with column names of df as index and series values as datatypes of the columns
type(nba.dtypes)

nba.dtypes.value_counts()  # running method on series which is output of dtypes method to check how many columns are there of each type, called method chaining, nice way of getting to know the data types of each column of df
# for numeric/whole number column when there is NaN present then its stored automatically as floating point type
type(nba.dtypes.value_counts())
print(nba.dtypes.value_counts())

nba.columns  # gives all the headers of dataframe columns as a index object
type(nba.columns)

nba.axes  # gives both indexes of dataframe

nba.info()  # gives all the exes and summary in a single output dataframe, helps us compare all the columns side by side, give non null count and dtype both. memory usage is the amount of RAM that is used by this series in computer

# columns in itself is a separate index that stores labels for each column. This can be numeric of string.
