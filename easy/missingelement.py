'''
CHALLENGE: FIND MISSING ELEMENTS IN ARRAY
Given an array of integers, find the missing elements within the min and max elements of the array

EXAMPLE
Given the following array, you will get
missing_element([2,3,5,6,10]) => [4,7,8,9]
missing_element([10,14,16]) => [11,12,13,15]
missing_element([1,2,3,6]) => [4,5]
'''
from nose.tools import assert_equal

# SOLUTION 1: Using list comprehension


def missing_element1(arr):  # O(n)
    return [a for a in range(arr[0], max(arr)) if a not in arr]


# SOLUTION 2: Using set, however this will work only when there is no duplicates
def missing_element2(arr):  # O(1)
    return sorted(set(range(min(arr), max(arr))) - set(arr))


# SOLUTION 3: Using difference method, will work when there is no consideration for duplicates
def missing_element3(arr):  # O(1)
    return sorted(set(range(min(arr), max(arr))).difference(arr))


# Test class function
class TestMissingElements(object):

    def test(self, solution):
        assert_equal(solution([2, 3, 5, 6, 10]), [4, 7, 8, 9])
        assert_equal(solution([10, 14, 16]), [11, 12, 13, 15])
        assert_equal(solution([1, 2, 3, 6]), [4, 5])
        print('All test cases passed')


# Run tests
t = TestMissingElements()
t.test(missing_element1)
