"""
SORT COLORS
https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue, sort them in-place 
so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""


# SOLUTION 1: Using quick sort partition with pointers to sort values
# O(N) TIME AND O(1) SPACE
def sortColors(nums: list[int]) -> list[int]:
    """
    Initialize left, right pointers and i index
    loop through the array and for every value equal to 0, swap with i and increment pointer.
    For every value equal to 2, swap with i and increment right pointer but not i index(edge case)
    1 values will automatically be in middle if all 0s are to the left and all 2s to the right
    """
    l, r = 0, len(nums) - 1
    i = 0
    while i <= r:
        if nums[i] == 0:
            swap(nums, l, i)
            l += 1
        elif nums[i] == 2:
            swap(nums, i, r)
            r -= 1
            i -= 1
        i += 1
    return nums


def swap(nums, l, r):
    nums[l], nums[r] = nums[r], nums[l]
    return nums
