"""
GROUP ANAGRAMS
https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""
#SOLUTION 1: Using ord to get the no of letter in alphabet and using hashmap to store the anagrams
#O(MN) with m-no of strs and n->avg no of len of letters in strs && O(N) SPACE
from collections import defaultdict
def groupAnagrams1(strs):
  map = defaultdict(list)

  for st in strs:
    count = [0] * 26
    for s in st:
        count[ord(s) - ord("a")] += 1
    map[tuple(count)].append(st)
#   breakpoint()  
  return list(map.values())

#SOLUTION 2: Sorting the strs and using hashmap to collect the anagrams
#O(M*NLOGN) TIME AND O(MN) SPACE
def groupAnagrams2(strs):
  hashmap = {}

  for st in strs:
    sortedword = "".join(sorted(st))
    if sortedword in hashmap:
        hashmap[sortedword].append(st)
    else:
        hashmap[sortedword] = [st]
#   breakpoint()
  return list(hashmap.values())
