"""
ISOMOPHIC STRINGS
https://leetcode.com/problems/isomorphic-strings/
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
"""
#SOLUTION 1: Use two hashmap to store the values and compare with adjacent characters
#O(N) TIME AND O(N) SPACE
def isIsomorphic(s:str, t:str)->bool:
  """
  Initialize two hashmaps. Loop through the elements of str
  Add element in s to mapS and element in t to mapT
  Check if element in s is in mapS and compare if its isomorphic. Likewise,do same for element in t
  """
  mapS, mapT = {},{}
  for i,j in zip(s,t):
    if ((i in mapS and mapS[i] != j) or (j in mapT and mapT[j] != i)):
        return False
    mapS[i] = j
    mapT[j] = i
  return True