"""
REVERSE A STRING
https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""


# SOLUTION 1: Using pointers
# O(N) TIME AND O(1) SPACE
def reverse1(st):
    left, right = 0, len(st) - 1
    while left <= right:
        st[left], st[right] = st[right], st[left]
        left += 1
        right -= 1
    return st


# SOLUTION 2: Using iteration
# O(N) TIME AND O(1) SPACE
def reverse2(st):
    n = len(st)
    for i in range(0, n // 2):
        st[i], st[n - i - 1] = st[n - i - 1], st[i]
    return st


# SOLUTION 3: Using Stack data structure
# O(N) TIME AND O(N) SPACE
def reverse3(st):
    stack = []
    for s in st:
        stack.append(s)

    idx = 0
    while stack:
        st[idx] = stack.pop()
        idx += 1
    return st
