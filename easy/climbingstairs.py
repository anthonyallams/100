"""
CLIMBING STAIRS
https://leetcode.com/problems/climbing-stairs/
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
#SOLUTION 1: Using dp programming
#O(N) TIME AND O(1) SPACE
def climbStairs1(n):
  if n <= 3:
    return n
  n1, n2 = 2,3
  for i in range(4, n+1):
    temp = n1 + n2
    n1,n2 = n2, temp
  return n2

#SOLUTION 2: Using recursion with memoization
#O(N) TIME AND O(N) SPACE
def climbStairs2(n):
    memoize = {2:2, 3:3}
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = climbStairs2(n-1) + climbStairs2(n-2)
        return memoize[n]


#SOLUTION 3:Using brute force/recusion
#(2^N) TIME AND O(N) SPACE
def climbStairs3(n):
    if n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return climbStairs3(n-1) + climbStairs3(n-2)