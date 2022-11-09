"""
VALID PARENTHESIS
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if: Open brackets must be closed by the same type of brackets.
&& Open brackets must be closed in the correct order.
"""
#SOLUTION 1: Using hashmap and stack data structure
#O(N) TIME AND O(N) SPACE
def isValid1(s):
    map = map = {")":"(","]":"[","}":"{"}
    stack = []
    for char in s:
        if char not in map:
            stack.append(char)
            continue
        if not stack or map[char] != stack[-1]:
            return False
        stack.pop()
    return stack == []