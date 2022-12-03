"""
LONGEST COMMON PREFIX
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
#SOLUTION 1: Using iterative approach to loop through the first elem in array and compare the ith element of first element to the ith element of subsequent elements
#O(NM) TIME AND O(N) SPACE
def longestCommonPrefix(strs:list[str]) -> str :
        """
        Initialize an empty string, result
        Loop through the len of the first element iin array and for the i,
        Then loop through all elements in array
        Check if ith element of first array is equal to ith element of subsequent array
        Check if index is equal to the len of subsequent array for elements incase len of element is smaller than other elements in the array
        Then add the ith element to container 
        """
        result = ""
        for i in range(len(strs[0])):
            for st in strs:
                if i == len(st) or st[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result