"""
BINARY SEARCH
https://leetcode.com/problems/binary-search/
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""
#SOLUTION 1: Using pointers
#O(N LOGN) TIME AND O(1) SPACE
def binarysearch(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right)// 2
        if nums[mid] == target:
            return mid
        elif nums[mid]> target:
            right = mid - 1
        else:
            left = mid + 1
    return -1