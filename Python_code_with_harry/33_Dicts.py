#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 22:12:27 2025

@author: Rishabh_Tyagi
"""

"""
https://www.youtube.com/watch?v=j2G68uQtOwM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=33

Dictionaries in Python | Python Tutorial - Day #33
"""

"""
we can see values corresponding to a key like a real world dictionary. Access is very fast in it.

Dictionary are ordered collection of data items.
THey store mul;tiple items in a single variable.
Dict items are key value pairs that are separated by commas enclosed within curly brackets.


Ordered mean - when we print the keys they will always appear in ordered way

info[] gives error if key is not present in dict 
info.get() return none of key do not exist
"""

dic = {
       344: "Harry",
       56: "Shubham",
       678: "Zakir",
       567: "Neha"
       }

info = {
        'name':'Karan',
        'age':18,
        'eligible':True
        }


info['name'] # print value of info key from dict
info['age']
info['eligible']

info.get('name') # another way of getting value of a key

# info[] gives error if key is not present in dict 
# info.get() return none of key do not exist


info # gives all keys

# print all keys by iterating over keys
for key in info.keys():
    print(key)

info.values() # gives all values

for key in info.keys():
    print(f'value corresponding to key {key} -> {info[key]}')


info.items() # gives all key-value pairs

for i in info.items():
    print(i)


# here tuple of key value will be unpacked by looping over dict
for key, val in info.items():
    print(f"key is '{key}' and its value is '{val}'")
