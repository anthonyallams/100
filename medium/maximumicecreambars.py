"""
MAXIMUM ICE CREAM BARS
https://leetcode.com/problems/maximum-ice-cream-bars/
It is a sweltering summer day, and a boy wants to buy some ice cream bars.
At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] 
is the price of the ith ice cream bar in coins. 
The boy initially has "coins" coins to spend, and he wants to buy as many ice cream bars as possible. 
Note: The boy can buy the ice cream bars in any order.
Return the maximum number of ice cream bars the boy can buy with "coins" coins.
You must solve the problem by counting sort.

Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

Example 2:
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.

Example 3:
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
"""


# SOLUTION 1: Using sort method
# O(NLOGN) TIME AND O(1) SPACE
def maxIceCream(costs: list[int], coins: int) -> int:
    costs.sort()
    result = 0

    for i, c in enumerate(costs):
        result += c
        if result > coins:
            return i
    return len(costs)


# SOLUTION 2: Using inbuilt python methods: sorted, accumulate & bisect
from bisect import bisect
from itertools import accumulate


def maxIceCream2(costs: list[int], coins: int) -> int:
    """
    bisect method finds the position in a sorted list where a number can be inserted without distorting the sort order of the list eg: bisect([1,3,4],2)->[1,2,3,4]
    accumulate returns a running total/successive values of a list [1,2,3,4]->[1,3,6,10]
    """
    return bisect(list(accumulate(sorted(costs))), coins)
