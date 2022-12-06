"""
Majority element
https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Follow up: Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
#SOLUTION 1: Using Boyer moores algorithm
#O(N) TIME AND O(1) SPACE
def majorityElement(nums):
  """
  Add 1 to count if element occurs, else decrement count
  """
  res, count = 0,0
  for num in nums:
    if count == 0:
        res = num
    
    count += 1 if res == num else res
  return res


#SOLUTION 2: Using hashmap
#O(N) TIME AND O(N) SPACE
def majorityElement1(nums):
    """
    Initialize a hashmap and add the count of elements as values
    Get the key with max element
    """
    count = {}
    res, maxcount = 0,0

    for num in nums:
        count[num] = 1 + count.get(num, 0)
        res = num if count[num] > maxcount else res
        maxcount = max(maxcount, count[num])
    return res