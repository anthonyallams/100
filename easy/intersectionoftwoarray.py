"""
Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
#SOLUTION 1: Using  Counter
#O(N.M) TIME AND O(N.M) SPACE
from collections import Counter
def intersect(nums1:list[int],nums2:list[int])->list[int]:
  """
  Make sure that nums1 is has the less values by comparing and swapping values
  Get a count of array values using Counter and initialize a result array
  Iterate through the larger array, nums2 and check if the elem/key is in c1 and > 0
  If true, add to res array and minimize the values of key
  """
  n1, n2 = len(nums1), len(nums2)

  if n1 > n2:
    nums2, nums1 = nums1, nums2

  c1 = Counter(nums1)
  res = []

  for num in nums2:
    if num in c1 and c1[num]>0:
        res.append(num)
        c1[num] -= 1
  return res

#SOLUTION 2: Using pointer
#O(NLOGN) TIME COS OF SORT FUNCTION
def intersect1(nums1:list[int],nums2:list[int])->list[int]:
    """
    Sort the arrays for ease of comparison. Initialize i and j indices
    Loop through arrays and compare the individual values using i and j pointers
    When values match, append and increment
    """
    nums1.sort()
    nums2.sort()

    n1,n2 = len(nums1), len(nums2)
    i = j = 0

    res = []
    while i < n1 and j < n2:
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i, j = i+1, j+1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return res


