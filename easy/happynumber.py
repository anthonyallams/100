"""
#HAPPY NUMBER
#https://leetcode.com/problems/happy-number/
#Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not.
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Input: n = 2
# Output: false
"""


# SOLUTION 1: Using bit manipulation to calculate the sumofSquares
# O(N) TIME AND O(N) SPACE COS OF HASHSET
def isHappy(n):
    """
    Fist initialize a hashset to hold the sum of squares,
    if the sum of squares starting from n is not in the set,add it,
    and if the result of sum of squares is 1, then the number is happy.
    If the n is already in the hashset, n is not happy, as this is infinite loop
    """
    container = set()
    while n not in container:
        container.add(n)
        n = sumOfSquares(n)
    return n == 1


def sumOfSquares(n):
    output = 0
    while n:
        digit = n % 10
        digit = digit**2
        output += digit
        n //= 10

    return output
