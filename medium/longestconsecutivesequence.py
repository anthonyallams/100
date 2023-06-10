"""
LONGEST CONSECUTIVE SEQUENCE
https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


# SOLUTION 1: Using iterative approach and set to get the firest element in sequence and count consecutive sequence element length
# O(N) TIME AND O(N) SPACE
def longestConsecutive(nums):
    """
    Store the element in a set and define the longest variable
    Loop through the array and
    check if the element is the first in a sequence by comparing to elems in set
    If it's the first elem in a sequence, init a length variable and check the next n elements, add up the length
    Get the longest sequence length by getting the max of successive longest and the length
    """
    numset = set(nums)
    longest = 0

    for num in nums:
        if not (num - 1) in numset:
            length = 1
            while (num + length) in numset:
                length += 1
            longest = max(length, longest)
    return longest
