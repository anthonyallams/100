'''
CHALLENGE: LARGEST CONTIGUOUS SUM
Given an array of integers (positive and negative) find the largest continuous sum

EXAMPLE
Given the array, the largest subarray sum will be 29
large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
'''


from distutils.log import error
from nose.tools import assert_equal

# SOLUTION 1: Using Kadane's algorithm to compare current sum and maximum sum values of the array


def largest_cont_sum1(arr):  # O(n)

    # Check if the array has elements to start with
    if len(arr) == 0:
        return error

    # Initialize the current sum and maximum sum to 1st element of array
    curr_sum = max_sum = arr[0]

    # Loop through the array
    # Add each array element to current sum and compare current sum and array element
    # The higher value between current sum and array element becomes current sum
    # Compare current sum and maximum cum, the higher value becomes maximum sum
    for i in arr[1:]:
        curr_sum = max(curr_sum + i, i)
        max_sum = max(curr_sum, max_sum)
    return max_sum


class TestLargestContinuousSum(object):
    def test(self, solution):
        assert_equal(solution([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(solution([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(solution([-1, 1]), 1)
        print('All test cases passed')


t = TestLargestContinuousSum()
t.test(largest_cont_sum1)
