'''
CHALLENGE: Array Pair sum
Given an integer array, output all the unique pairs that sum up to a specific value k and the length

EXAMPLE
Given pair_sum([1,3,2,2],4) would return 2 pairs:
(1,3)
(2,2)
'''
# SOLUTION 1: Using sets for tracking and looping through array


from nose.tools import assert_equal
from distutils.log import error


def array_pair_sum(arr, k):  # O(n)
    # Ensure there are at least a pair in the array/list
    if len(arr) < 2:
        return error

    # Initialize sets for seen array elements and output tuples
    seen = set()
    output = set()

    # Loop through the elements in array(arr)
    # Subtract k from each arr element and store as num
    # If num is not in seen, add element else add the tuple to output set
    for i in arr:
        num = k - i

        if num not in seen:
            seen.add(i)
        else:
            output.add((min(i, num), max(i, num)))
    print(*list(output), sep='\n')
    return len(output)


# Test class function

class TestArrayPairSum(object):
    def test(self, solution):
        assert_equal(solution([1, 3, 2, 2], 4), 2)
        assert_equal(solution([1, 2, 3, 1], 3), 1)
        assert_equal(
            solution([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        print('All tests passed')


# Run test suite
t = TestArrayPairSum()
t.test(array_pair_sum)
