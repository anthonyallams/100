"""
CHALLENGE: Fibonacci Sequence
Print out the n-th entry in the fibonacci series. 
The fibonacci series is an ordering of numbers where each number is the sum of the preceeding two. 
Following is the first 10 fibonacci series: [0,1,1,2,3,5,8,13,21,34,55]

EXAMPLE: Given the following integers,  we would get the nth entry fibonacci as:
fibonacci(10) ==> 55
fibonacci(3) ==> 2
fibonacci(8) ==> 21
fibonacci(9) ==> 34
"""


# SOLUTION 1: Iterative approach
# O(N) TIME AND O(N) SPACE
def fibonacci1(n):
    # Initialize the initial fibonacci sequence to be 0 & 1
    a, b = 0, 1

    # Loop through from 2 to n-th value
    # Add 2 previous values since fibonacci is gotten by adding the 2 successive values  and return the last value of n
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b


# SOLUTION 2: Using recursion
# O(2^N) TIME AND O(N) SPACE COS OF RECURSION
def fibonacci2(n):
    # Check the edge case
    # Since fibonacci of 0 & 1 are constant, return n if its 0 or 1
    if n == 1 or n == 2:
        return 1
    # Recursively call fibonacci on previous 2 entries till it returns to the nth-entry
    return fibonacci2(n - 1) + fibonacci2(n - 2)


# SOLUTION 3: Using recursion with memoization
# O(N) TIME AND O(N) SPACE
def fibonacci3(n):
    memoize = {0: 0, 1: 1}
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fibonacci3(n - 1) + fibonacci3(n - 2)
        return memoize[n]
