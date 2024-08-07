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


# we can provide the index where we want to place our new column in insert method, it will shift rest of the columns right
nba.insert(loc=3, column = 'Sport', value = 'Basketball')


# Value counts method coutns the number of times a unique value occurs in a col
nba['Team']
nba['Team'].value_counts()
nba['Position'].value_counts(normalize=True) * 100 # this gives the percentages each value is part of the total values




## ---- Additonal snippets ---- ##
#--------------------
import pandas as pd
pd.set_option('display.max_columns', None) # pandas setting to force terminal to display all columns of dataframe
pd.set_option('display.max_rows', None) # pandas setting to force terminal to display all rows of dataframe

df = pd.read_csv("")
df.head(5)

df.info()
df.describe()

# Events have 9 values only, get count of rows for each of these 9 values
# get count of nulls in Events columns

# What is 25 percentile, 50 percentile, 75 percentile thoeretically 

df['EST'] = pd.to_datetime(df['EST']) # converting column type from object type to Datetime

df['EST'].max()

#---------------------------------------------------#
# Reading excel and then its individual sheets as df
df = pd.read_excel("excel_file.xlsx","Sheet1")


# Reading data from dict as dataframe
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017','1/7/2017','1/8/2017'],
    'temp': [32,35,28,24,32,31,17,29],
    'windspeed': [6,7,2,7,4,2,11,6],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny','Snow','Rain'],
    'humidity': [6.5,0,2.7,7.4,4.3,11,'','NaN'],
    'aqi': [6.5,0,2.7,7.4,4.3,11,200,300],
}
df = pd.DataFrame(weather_data)
df


# Reading data from tuple list as dataframe
weather_data2 = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]

dft = pd.DataFrame(weather_data2, columns=['day','temp','windspeed','event'])
dft


# Skip 1 row when reading data from csv/excel(when extra headers in file)
dft = pd.DataFrame("weather_data.csv", skiprows=1)
# or
dft = pd.DataFrame("weather_data.csv", header=1)
dft

# when csv file do not have any header, auto column names will be generated so pass names argument with column names
df = pd.DataFrame("weather_data.csv", header=None, names=['day','temp','windspeed','event'])
df


# when we want to read only n number of rows from csv
df = pd.DataFrame("weather_data.csv", header=1, nrows = 3)
df
# this will read 3 rows from csv excluding header


# when there are some bad data and we want to read it as NaN then we can pass argument to na_values
dfx = pd.read_csv("/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/02_Sample_datasets/9_weather_data2.csv", na_values=['not available','n.a.'])
dfx
# this will read data and then set NaN and then create df with right datatypes


# if we want to convert bad data of only specific column to Nan we can supply dict to na_values method.
dfx = pd.read_csv("/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/02_Sample_datasets/9_weather_data2.csv",
                  na_values={
                      'temp' : ['not available','n.a.'],
                      'windspeed' : [-1]
                  }
                  )
dfx


# Writing csv to local
df.to_csv('op_data.csv', index=False)

# writing csv with only limited number of cols
df.to_csv('op_data.csv', index=False, columns = ['day','temp'])


# read excel and convert some bad data to some other value using converters.
def convert_people_cell(cell):
    if cell=="n.a.":
        return 'Sam Walton'
    return cell

def convert_price_cell(cell):
    if cell=="n.a.":
        return 50
    return cell
    
df = pd.read_excel("stock_data.xlsx","Sheet1", converters= {
        'people': convert_people_cell,
        'price': convert_price_cell
    })
df

# write to excel but start writing from 2nd row of excel sheet
df.to_excel("new.xlsx", sheet_name="stocks", index=False, startrow=2, startcol=1)


# writing to two sheets of one excel
df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})
# https://github.com/codebasics/py/blob/master/pandas/4_read_write_to_excel/read_write_csv_excel.ipynb



data = [
['0', 'Y', 'N'], 
['1', 'Y', 'Y'], 
['2', 'N', 'Y'], 
['3', 'Y', 'Y'], 
['4', 'N', 'N']
]
products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})



# To explicity read any column as data type we can use parse_dates while reading the csv
df = pd.read_csv("/Users/Rishabh_Tyagi/Box Sync/1_RT_docs/2_My_py_projects/0_Python_RT/02_Sample_datasets/10_weather_data3.csv"
                ,parse_dates=['day'])
df


# fill/replace all NaN values with 0
df.fillna(0) 



# fill Nan values of different columns with different values by passing a dict to fillna method
df.fillna({
    'temp':0,
    'windspeed':0.0,
    'event':'No Event'
})


# filling with 0 in temp is not sensible, also it will skew the mean, we can fill it with more sensible value.

# one way could be to fill NaN values of any column with previous/last value
# this is called forward fill
df.fillna(method = 'ffill') # this is little better than having 0 for all blanks


# this is called forward fill
df.fillna(method = 'bfill')
# or
df.fillna(method = 'backfill')

# using axis will fill NaN with right column values
# if there is no value in left most column it will remain NaN
df.fillna(method = 'backfill', axis = 'columns')

# when I want to copy only once or to fill only one blank value
df.fillna(method = 'backfill', limit =1)

# Pandas fill the NaN values by using linear interpolation
df.interpolate()
