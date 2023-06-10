"""
COUNT THE DIGITS THAT DIVIDE A NUMBER
https://leetcode.com/problems/count-the-digits-that-divide-a-number/
Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.

Example 1:
Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.

Example 2:
Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2

Example 3:
Input: num = 1248
Output: 4
Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
"""


# SOLUTION 1: Iterative approach
# O(N) TIME AND O(1) SPACE
def countDigits(num: int):
    result = 0
    for n in str(num):
        if num % int(n) == 0:
            result += 1
    return result


def countDigits(num: int):
    return sum(num % int(n) == 0 for n in str(num))
