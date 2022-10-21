"""
PALINDROME NUMBER
https://leetcode.com/problems/palindrome-number/
Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the same backward as forward.
"""
#SOLUTION 1: Using iterable 
#O(N) TIME AND O(N) SPACE
def isPalindrome1(nums):
    nums= str(nums)
    reversed_num = ''.join([num for num in reversed(nums)])
    return nums == reversed_num

#SOLUTION 2: Using pointers
#O(N) TIME AND O(N) SPACE
def isPalindrome2(nums):
    nums= str(nums)
    left, right = 0, len(str(nums))-1
    while left <= right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1
    return True


