"""
COUNTING BITS
https://leetcode.com/problems/counting-bits/
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Input: n = 5
Output: [0,1,1,2,1,2]
FOLLOWUP:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
"""
#SOLUTION 1: Using dynamic programming
#O(N) TIME AND O(N) SPACE
def countBits1(n):
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1,n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp

#SOLUTION 2: Using iterative approach to count the number of 1 bits in each n value
#O(N) TIME AND O(N) SPACE
def countBits2(n):
    output = [0]
    for i in range(n+1):
        output.extend([i+1 for i in output])
    return output[:n+1]
