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
def groupAnagrams1(strs:list[str])->list[list[str]]:
  """
  Initialize a hashmap of default k,v pairs using defaultdict
  Loop through the list of strings and initialize count as no of letters in English alphabets
  Loop through each letter in word and increment if letter is in count
  Add a tuple of count to the hashmap as key and the list of words as value
  """
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
def groupAnagrams2(strs:list[str])->list[list[str]]:
  """
  Initialize hashmap
  Loop through the array of strings and for each string, pass through sorted method
  Add sorted word into hashmap as key and string element as value
  Return the values of hashmap
  """
  hashmap = {}

  for st in strs:
    sortedword = "".join(sorted(st))
    if sortedword in hashmap:
        hashmap[sortedword].append(st)
    else:
        hashmap[sortedword] = [st]
#   breakpoint()
  return list(hashmap.values())
