"""
3SUM PROBLEM
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
#SOLUTION 1: Using two loops: First to get the first element and 2nd to perform a two sum(pointer operation) on the remaining two elements
#O(N^2) TIME AND O(N) SPACE
def threeSum1(nums):
  result = []
  nums.sort()
  for i in range(len(nums)-1):
    if i > 0 and nums[i] == nums[i-1]:
      continue

    l,r = i+1, len(nums)-1
    while l < r:
      cursum = nums[i] + nums[l] + nums[r]
      if cursum == 0:
        result.append([nums[i], nums[l], nums[r]])
        l,r = l+1, r-1
      elif cursum > 0:
        r -= 1
      else:
        l += 1
  return result