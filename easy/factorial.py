'''
Create a function that computes the factorial of an integer
5! = 5*4*3*2*1 => 120
'''
import numpy as np
# SOLUTION 1: Using a for-loop, #O(n)


def factorial(n):
    fact = 1
    # Taking care of edge case where input is 0
    if n == 0:
        return 1
    # Loop through 1 to n+1, and multiple successive values from 1 to n
    for i in range(1, n+1):
        fact *= i
    return fact


# SOLUTION 2: Using recursion
def factorial2(n):
    # Take care of recursion base case where n = 0
    if n == 0:
        return 1
    else:
        # Return value of n and successive preceding factorials
        return n * factorial2(n-1)


# SOLUTION 3: Using numpy module
# First import numpy module
def factorial3(n):
    if n == 0:
        return 1
    else:
        return np.prod(np.arange(1, n+1))


print(factorial(3))
print(factorial2(5))
print(factorial3(5))
