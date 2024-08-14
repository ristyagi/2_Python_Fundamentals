#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:00:37 2024

@author: ristyagi@gmail.com
"""

import pandas as pd


#01-------------------------------------------------------
# convert columns to correct datatypes, this reduces memory space taken by df

emp = pd.read_csv("pandas/Complete/employees.csv")
emp
emp.info()
emp.describe()
emp.dtypes
emp.columns
emp.shape
emp['Gender'].value_counts()
emp['Gender'].value_counts(dropna = False)
emp['Gender'].nunique()
emp['Gender'].unique()
emp['Gender'] = emp['Gender'].fillna(value = 'Gender not available')
emp['Gender'].count()
emp['Senior Management'].value_counts(dropna = False)
emp['Team'].value_counts(dropna = False)

# pandas read any date column as object first we need to force datetype on such columns, this also reduces the memory usage
# also so that date realted methods can work on such cols

emp['Start Date']
pd.to_datetime(emp['Start Date'], format = '%m/%d/%Y') # format here is the format of existing date, so that pandas do no confuse month with day while converting.

# pd.to_datetime(emp['Start Date'], format = '%m-%d-%Y')
emp['Start Date'] = pd.to_datetime(emp['Start Date'], format = '%m/%d/%Y')
emp['Start Date']

pd.to_datetime(emp['Last Login Time']) # warning by pandas as we have not specified the format
pd.to_datetime(emp['Last Login Time'], format = '%H:%M %p') # since explicit date was not there, pandas automatically added default date, %p is used to specify am/pm value

pd.to_datetime(emp['Last Login Time'], format = '%H:%M %p').dt.time # dt.time object gives time component only

emp['Last Login Time'] = pd.to_datetime(emp['Last Login Time'], format = '%H:%M %p').dt.time

emp['Last Login Time']

emp.info()

emp['Senior Management'].value_counts(dropna = False)

emp['Senior Management'] = emp['Senior Management'].astype('bool') # this converted NaN values as TRUE, which is not right

emp['Gender'] = emp['Gender'].astype('category') # this do not force change Nan to anything, keeps them as NaN

emp['Gender'].value_counts(dropna = False)


# directly reading csv and parse dates
emp = pd.read_csv("pandas/Complete/employees.csv", parse_dates = ['Start Date'], date_format = '%m/%d/%Y')
emp.info()



#02-------------------------------------------------------
# Filter dataframe data based on a condtion

emp = pd.read_csv("pandas/Complete/employees.csv", parse_dates = ['Start Date'], date_format = '%m/%d/%Y')
emp
emp.info()

emp['Senior Management'].value_counts(dropna = False)
emp['Team'].value_counts(dropna = False)

emp['Last Login Time'] = pd.to_datetime(emp['Last Login Time'], format = '%H:%M %p').dt.time
# emp['Senior Management'] = emp['Senior Management'].astype('bool') # converted senior management to bool as anyway emp where this col is NaN will not be a senior management person,but after bool it will convert to True which is not right
emp['Senior Management'] = emp['Senior Management'].astype('category') # converting it to category will retain NaNs
emp['Gender'] = emp['Gender'].astype('category')
emp['Team'] = emp['Team'].astype('category')
emp.info()

emp['Gender'].value_counts(dropna = False)

emp[emp['Gender'] == 'Male'] # this will pull out only those df rows where gender is Male

emp['Team'].value_counts(dropna = False) # 102 records in Finance
emp[emp['Team'] == 'Finance'] # only 102 rows where team = Finance are pulled

filter_cndtn = emp['Team'] == 'Finance' # make filter condition and pass it to df
emp[filter_cndtn]

# How to get those rows from df where value of col in NaN
# emp[emp['Team'] == 'NaN']

emp[emp['Senior Management'] == True]

emp[emp['Salary'] > 11000] ## all emp having salary > 110k

emp[emp['Bonus %'] <=1.1]

emp[emp['Start Date'] == '1996-03-31']

import datetime as dt

emp[emp['Last Login Time'] < dt.time(12, 0, 0)] # all emo who logged in before noon, compared only time column with time value only


#03-------------------------------------------------------
# Filter dataframe with one or more conditions

emp = pd.read_csv("pandas/Complete/employees.csv", parse_dates = ['Start Date'], date_format = '%m/%d/%Y')
emp
emp['Last Login Time'] = pd.to_datetime(emp['Last Login Time'], format = '%H:%M %p').dt.time
emp['Senior Management'] = emp['Senior Management'].astype('bool')
emp['Gender'] = emp['Gender'].astype('category')
emp['Team'] = emp['Team'].astype('category')
emp.info()


emp['Gender'].unique()

is_female = emp['Gender'] == 'Female'
is_in_marketing = emp['Team'] == 'Marketing'

emp[is_female & is_in_marketing] # filtering with two conditions

# emp['First Name'].iloc[62]

emp.head()
emp.info()

emp[(emp['First Name'] == 'Douglas') & (emp['Salary'] == 97308)] # filter with two cndtns

emp[((emp['First Name'] == 'Douglas') 
    | (emp['First Name'] == 'Thomas'))
    & (emp['Gender'] == 'Male')]


name_cdtn = emp['First Name'] == 'Douglas'
name_cdtn2 = emp['First Name'] == 'Thomas'
gender_cndtn = emp['Gender'] == 'Male'

emp[name_cdtn | name_cdtn2 & gender_cndtn]
emp[(name_cdtn2 & gender_cndtn) | name_cdtn]


#04-------------------------------------------------------
# isin and not in Method

emp.info()
ls = list(emp['Team'].unique())
ls
emp['Team'].value_counts(dropna = False)
emp[~emp['Team'].isin(['Finance', 'Product', 'Sales'])]


fil = ~emp['Team'].isin(['Finance', 'Product', 'Sales'])
emp[fil]



#05-------------------------------------------------------
# isnull and notnull Method
# identify all records where NaN in a columns

emp[~emp['Team'].isnull()] # 43 rows where team is null as results
emp[~emp['Team'].notnull()]

emp[~emp['Team'].isnull()]
emp[~emp['Team'].notnull()] # 43 rows where team is null as results


emp.info()

emp['First Name'].isnull()
emp['Team'].isnull()

emp[emp['First Name'].isnull() & emp['Team'].isnull()]

# emp[['First Name','Salary']] # this is not going to result same as above


#06-------------------------------------------------------
# between Method

# to check each value of a col is between the range provided

