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
def isAnagram1(s:str,t:str)->bool:
    counts, countt = {},{}
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        counts[s[i]] = 1 + counts.get(s[i], 0)
        countt[t[i]] = 1 + countt.get(t[i], 0)
    
    for c in counts:
        if counts[c] != countt.get(c, 0):
            return False
    return True

#SOLUTION 2: Using python sorted
#O(N LOG N) TIME COMPLEXITY COS OF SORT METHOD AND O(1) SPACE COMPLEXITY
def isAnagram2(s:str,t:str)->bool:
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)

#SOLUTION 3: Using collections.Counter method
#O(N) TIME COMPLEXITY AND O(N) SPACE COMPLEXITY
from collections import Counter
def isAnagram3(s:str,t:str)->bool:
    return Counter(s) == Counter(t)

# In cases where non-alphanumeric sentence is provided rather than words
#SOLUTION 4: Using sort and regex to remove non-alphanumeric character
#O(NLOGN) TIME COS OF SORT METHOD AND O(1) SPACE 
import re
def isAnagram4(s:str,t:str)->bool:
    s1 = re.sub('[^\w]', '', ''.join(sorted(s.lower())))
    t1 = re.sub('[^\w]', '', ''.join(sorted(t.lower())))

    if len(s1) != len(t1):
        return False
    
    for i in range(len(s1)):
        if s1[i] != t1[i]:
            return False
    return True