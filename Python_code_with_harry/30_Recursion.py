#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 21:47:33 2025

@author: Rishabh_Tyagi
"""

"""
https://www.youtube.com/watch?v=XYwJKFB8DUk&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=30

Recursion in Python | Python Tutorial - Day #30

"""


"""
calling a function inside a function is called recursion

example where recursion can be used is factorial


factorial(6) = 6*5*4*3*2*1
factorial(5) = 5*4*3*2*1
factorial(0) = 1

this can be done like 
factorial(n) = n * factorial(n-1)

factorial(6) = 6*factorial(5)
factorial(5) = 5*factorial(4)..and do on
"""

def factorial(n):
    '''
    Parameters
    ----------
    n : integer
        value whose factorial needs to be calculated.

    Returns
    -------
    factorial of n.

    '''
    
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)


factorial(0)
factorial(1)
factorial(4)

# this is how recursion will work
# factorial(4)
# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2* factorial(1)
    

print(factorial.__doc__)



# calculation of fibonacci series

# f(0) = 0
# f(1) = 1
# f(2) = 1
# f(3) = 2
# f(n) = f(n-1) + f(n-2)

def fib(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(0)
fib(1)    
fib(2)
fib(3)
fib(4)
fib(5)


#####
"""
x^y


create recursive function to calculate x^y


"""

def power(x, y):
    print('This is main fn')
    if (x==0):
        print('x is zero')
        return x
    elif (y==0 or y==1):
        print('y is zero or one')
        return x
    else:
        return x * power(x, y-1)
    
power(0,0)
power(0,1)
power(1,0)
power(1,1)
power(2,0)
power(2,1)
power(2,2)
power(2,3)

power(5,3)
power(5,5)
