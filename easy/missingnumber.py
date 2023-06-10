"""
MISSING NUMBER
https://leetcode.com/problems/missing-number/
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""


# SOLUTION 1: Subtracting the sum of nums from sum of range of length of nums
# O(N) TIME AND O(1) SPACE
def missingNumber1(nums):
    result = len(nums)
    for i in range(len(nums)):
        result += i - nums[i]
    return result


# SOLUTION 2: Using XOR bit manipulation to get missing number
# O(N) TIME AND O(1) SPACE
def missingNumber2(nums):
    result = len(nums)
    for i in range(len(nums)):
        result ^= i ^ nums[i]
    return result


# SOLUTION 3: Using hashmap to get the missing number
# O(N) TIME AND O(N) SPACE
def missingNumber3(nums):
    map = {}
    for num in nums:
        map[num] = 1 + map.get(num, 0)

    for idx in range(len(nums)):
        if idx not in map:
            return idx
