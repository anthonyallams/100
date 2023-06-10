"""
TOP K FREQUENT ELEMENTS
https://leetcode.com/problems/top-k-frequent-elements/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""


# SOLUTION 1: Using hashmap to get count and a list of lists to get get the occurrence of the numbes
# O(N) TIME AND O(N) SPACE
def topKFrequent(nums, k):
    """
    ALGORITHM:
    Use a hashmap to get the occurence of the num in nums
    Loop through the hashmap and add the num in nums(values) into index of key
    Loop through the frequency list in reverse order and append the k elements to result list, checking if the length of result is equal to k
    """
    count = {}
    frequency = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for key, value in count.items():
        frequency[value].append(key)

    result = []
    for i in range(len(frequency) - 1, 0, -1):
        for n in frequency[i]:
            result.append(n)
            if len(result) == k:
                return result
