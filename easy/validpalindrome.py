"""
VALID PALINDROME
https://leetcode.com/problems/valid-palindrome/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
"""


# SOLUTION 1: Using inbuilt python methods for string reversal and to check for alphanumeric
# O(N) TIME AND O(N) SPACE
def isPalindrome1(s):
    output = "".join([elem for elem in s.lower() if elem.isalnum()])
    return output == output[::-1]


# SOLUTION 2: Using pointers and a helper function to decide to check for alphanumeric chars
# O(N) TIME AND O(1) SPACE
def isPalindrome2(s):
    left, right = 0, len(s) - 1
    while left <= right:
        while left < right and not isalpha(s[left]):
            left += 1
        while right > left and not isalpha(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def isalpha(elem):
    return "A" <= elem <= "Z" or "a" <= elem <= "z" or "0" <= elem <= "9"
