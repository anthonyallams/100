"""
MAXIMUM SUBARRAY
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. A subarray is a contiguous part of an array.
"""


# SOLUTION 1: Using kadane's algorithm
# O(N) TIME AND O(1) SPACE
def maxSubArray1(nums):
    maxSub = curSum = nums[0]

    for num in nums[1:]:
        curSum = max(curSum + num, num)
        maxSub = max(maxSub, curSum)
    return maxSub


# SOLUTION 1: Using kadane's algorithm but removing negative values
# O(N) TIME AND O(1) SPACE
def maxSubArray2(nums):
    maxSub, curSum = nums[0], 0
    for num in nums:
        if curSum < 0:
            curSum = 0
        curSum += num
        maxSub = max(maxSub, curSum)
    return maxSub
