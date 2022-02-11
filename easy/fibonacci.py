'''
CHALLENGE: Fibonacci Sequence
Print out the n-th entry in the fibonacci series. 
The fibonacci series is an ordering of numbers where each number is the sum of the preceeding two. 
Following is the first 10 fibonacci series: [0,1,1,2,3,5,8,13,21,34,55]

EXAMPLE: Given the following integers,  we would get the nth entry fibonacci as:
fibonacci(10) ==> 55
fibonacci(3) ==> 2
fibonacci(8) ==> 21
fibonacci(9) ==> 34
'''
from nose.tools import assert_equal

# SOLUTION 1: Using loop


def fibonacci1(n):  # O(n)
    # Initialize the initial fibonacci sequence to be 0 & 1
    a = 0
    b = 1

    # Loop through from 2 to n-th value
    # Add 2 previous values since fibonacci is gotten by adding the 2 successive values  and return the last value of n
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b


# SOLUTION 2: Using recursion
def fibonacci2(n):
    # Check the edge case
    # Since fibonacci of 0 & 1 are constant, return n if its 0 or 1
    if n == 1 or n == 2:
        return 1
    # Recursively call fibonacci on previous 2 entries till it returns to the nth-entry
    return fibonacci2(n-1) + fibonacci2(n-2)

# Test class function


class TestFibonacci(object):

    def test(self, solution):
        assert_equal(solution(10), 55)
        assert_equal(solution(3), 2)
        assert_equal(solution(8), 21)
        assert_equal(solution(9), 34)
        print('All test cases passed')


# Run tests
t = TestFibonacci()
t.test(fibonacci2)
