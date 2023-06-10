"""
SINGLE NUMBER
https://leetcode.com/problems/single-number/ 136
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


# SOLUTION 1:Using XOR operator to get element that appears once
# O(N) TIME AND O(1) SPACE
def singleNumber1(nums):
    result = 0
    for num in nums:
        result = result ^ num
    return result


# SOLUTION 2: Using hashmap to get occurence of numbers
# O(N) time and O(N) TIME
def singleNumber2(nums):
    counter = {}
    for num in nums:
        counter[num] = 1 + counter.get(num, 0)

    for c in counter:
        if counter[c] != 2:
            return c
