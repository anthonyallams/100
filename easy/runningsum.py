"""
9TH JANUARY 2022
RUNNING SUM OF 1D ARRAY
https://leetcode.com/problems/running-sum-of-1d-array/description/
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""


# SOLUTION 1: Brute force
# O(N^2) TIME AND O(N) SPACE
def runningSum(nums: list[int]) -> list[int]:
    ans = []
    for i in range(len(nums)):
        runSum = 0
        for j in range(i + 1):
            runSum += nums[j]
        ans.append(runSum)
    return ans


# SOLUTION 2: One pass solution
# (O)N TIME AND O(N) SPACE
def runningSum1(nums: list[int]) -> list[int]:
    runSum = [nums[0]]
    for i in range(1, len(nums)):
        runSum.append(runSum[i - 1] + nums[i])
    return runSum


# SOLUTION 3: One pass solution
# O(N) TIME AND O(1) SPACE
def runningSum2(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return nums
