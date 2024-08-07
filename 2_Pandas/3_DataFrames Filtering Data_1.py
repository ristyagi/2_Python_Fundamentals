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
emp.info()

emp['Team'].value_counts(dropna = False)

emp['Last Login Time'] = pd.to_datetime(emp['Last Login Time'], format = '%H:%M %p').dt.time
emp['Senior Management'] = emp['Senior Management'].astype('category')
emp['Gender'] = emp['Gender'].astype('category')
emp['Team'] = emp['Team'].astype('category')
emp.info()

emp['Gender'].value_counts(dropna = False)

emp[emp['Gender'] == 'Male'] # this will pull out only those df rows where gender is Male

emp['Team'].value_counts(dropna = False)
emp[emp['Team'] == 'Finance'] # only 102 rows where team = Finance are pulled


