"""
Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Given an array nums of n integers where nums[i] is in the range [1, n], return an 
array of all the integers in the range [1, n] that do not appear in nums.
Follow up: Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
"""


# SOLUTION 1: Using iterative approach to map 1-n to 0-(n-1)
# O(N) TIME and O(1) SPACE
def findDisappearedNumbers(nums: list) -> list[int]:
    """
    ALGORITHM: Using a mapping of 1-n array elements to 0-(n-1) index in the array and multiply by -1
    Loop through the input array and
    For every value, subtract 1 & multiply -1 to get n=>(n-1) {1-n => 0-(n-1)} nums to index mapping
    Replace each elem in the input array with the result.
    Loop through elem array and for each positive value, add 1 to the index and return the index
    Postive values + 1 are the missing numbers in input array
    """
    for num in nums:
        i = abs(num) - 1
        nums[i] = -1 * abs(nums[i])

    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i + 1)
    return res


# SOLUTION 2: Removing the numbers not in the range from num
# O(N) TIME AND O(N) SPACE
def findDisappearedNumbers1(nums: list) -> list[int]:
    res = []
    for i in range(len(nums)):
        if i + 1 not in nums:
            res.append(i + 1)
    return res
