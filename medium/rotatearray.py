"""
Rotate Arrays
https://leetcode.com/problems/rotate-array/
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""


# SOLUTION 1: Using pointers to replace inplace based on position of k
# O(N) TIME AND O(1) SPACE (OPTIMAL SOLUTION)
def rotate(nums: list, k: int) -> list:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Reverse the entire array using replace helper function
    k = k % len(nums)
    l, r = 0, len(nums) - 1
    swap(nums, l, r)

    # Reverse the array from 0 to position k
    l, r = 0, k - 1
    swap(nums, l, r)

    # Reverse the array from position k to end
    l, r = k, len(nums) - 1
    swap(nums, l, r)

    return nums


def swap(nums: list, l: int, r: int) -> list:
    while l <= r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    return nums


# SOLUTION 2: Loop through the entire array and use (i+k) % len(nums) to replace elements
# O(N) TIME AND O(N) SPACE
def rotate1(nums: list, k: int) -> list:
    rotated = [0] * len(nums)
    for i in range(len(nums)):
        pos = (i + k) % len(nums)
        rotated[pos] = nums[i]
    return rotated


# SOLUTION 3: Pythonic solution
# O(N) TIME AND O(N) SPACE
def rotate2(nums: list, k: int) -> list:
    k = k % len(nums)  # To avoid rotations
    nums[:] = nums[-k:] + nums[:-k]
    return nums
