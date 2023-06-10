"""
CONTAINS DUPLICATE
https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


# SOUTION 1: Using hashmap/hashset to check for duplicates
# O(N) TIME AND O(N) SPACE
def containsduplicate1(nums):
    hashmap = {}
    for num in nums:
        if num in hashmap:
            return True
        hashmap[num] = 1
    return False


# SOLUTION 2: Using brute force method
# O(N^2) TIME AND O(1) SPACE
def containsduplicate2(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
