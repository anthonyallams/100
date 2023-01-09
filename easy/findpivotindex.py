"""
Find pivot Index
https://leetcode.com/problems/find-pivot-index/
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index 
is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because 
there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
"""
#SOLUTION ONE: Subtracting the rightSum from the total
#O(N) TIME AND O(1) SPACE
def pivotIndex(nums:list[int])->int:
  """
  ALGORITHM:
  Get the sum of elements in array as total and initialize the leftSum
  LeftSum is addition of consecutive elements in array
  Subtract the element and leftSum to get the right sum
  Loop through the array and for each iteration, get the rightSum
  Return index when rightSum == leftSum else return -1
  """
  total = sum(nums)
  leftSum = 0

  for i in range(len(nums)):
    rightSum = total - nums[i] - leftSum
    if rightSum == leftSum:
      return i
    leftSum += nums[i]
  return -1

#SOLUTION 2: Similar to 1
#O(N) TIME AND O(1) SPACE
def pivotIndex1(nums:list[int])->int:
  leftSum, rightSum = 0, sum(nums)
  for i in range(len(nums)):
    rightSum -= nums[i]
    if leftSum == rightSum:
      return i
    leftSum += nums[i]
  return -1

#SOLUTION 3: Bruteforce 
#O(N^2) TIME AND O(N) SPACE
def pivotIndex2(nums:list[int])->int:
  ans = []
  for i in range(len(nums)):
    if sum(nums[:i]) == sum(nums[i+1:]):
      return i
  return -1