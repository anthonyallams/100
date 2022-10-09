"""
VALID ANAGRAM
https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

EXAMPLE
Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "rat", t = "car"
Output: false
"""

#SOLUTION 1: Using hashmap to make counter for both string
#O(N) TIME COMPLEXITY AND O(N) SPACE COMPLEXITY
def isAnagram(s,t):
    counts, countt = {},{}
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        counts[s[i]] = 1 + counts.get(s[i], 0)
        countt[t[i]] = 1 + countt.get(s[i], 0)
    
    for c in counts:
        if counts[c] != countt.get(c, 0):
            return False
    return True

#SOLUTION 2: Using python sorted
#O(N LOG N) TIME COMPLEXITY AND O(N) SPACE COMPLEXITY
def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)

#SOLUTION 3: Using collections.Counter method
#O(N) TIME COMPLEXITY AND O(N) SPACE COMPLEXITY
from collections import Counter
def isAnagram(s,t):
    return Counter(s) == Counter(t)