#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 18:05:21 2025

@author: Rishabh_Tyagi
"""

"""
https://www.youtube.com/watch?v=LmbFwaLjT9k&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=35

Dictionary Methods in Python | Python Tutorial - Day #34
"""

"""
update method will ad second dict into first
clear method clears the entire dict
pop method removes key-value pair
pop item gives last itme of the dict
del deletes the dict, if key is not provided entire dict will be deleted

set is unordered in python
dict is ordered since python 3.7 onwards
key error comes when a key is provided which is not present in dict
dict documentation -> https://docs.python.org/2/tutorial/datastructures.html#dictionaries
"""

ep1  = {123: 34, 222: 67, 567: 90}
ep2  = {122: 45, 670: 69}

ep1.update(ep2)

ep1
ep1.clear()
ep1

empt = {} # empty dict
print(empt)

ep2.pop(122)
ep2

ep1.popitem()

del ep2
ep2

del ep1[567]
ep1


# https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions
dict2 = {x: x**2 for x in (2, 4, 6)}
dict2
