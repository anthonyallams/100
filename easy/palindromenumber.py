"""
PALINDROME NUMBER
https://leetcode.com/problems/palindrome-number/
Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the same backward as forward.
"""


# SOLUTION 1: Using iterable
# O(N) TIME AND O(N) SPACE
def isPalindrome1(nums):
    nums = str(nums)
    reversed_num = "".join([num for num in reversed(nums)])
    return nums == reversed_num


# SOLUTION 2: Using pointers
# O(N) TIME AND O(N) SPACE
def isPalindrome2(nums):
    nums = str(nums)
    left, right = 0, len(str(nums)) - 1
    while left <= right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1
    return True


# SOLUTION 3: Using integer operations
# O(N) TIME AND O(1) SPACE
def isPalindrome3(nums):
    if nums < 0 or (nums > 0 and nums % 10 == 0):
        return False
    div = 1
    while nums >= 10 * div:
        div *= 10
    while nums:
        right = nums % 10
        left = nums // div
        if left != right:
            return False
        nums = (nums % div) // 10
        div //= 100
    return True
