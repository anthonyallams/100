"""
CONTAINER WITH MOST WATER
https://leetcode.com/problems/container-with-most-water/
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""


# SOLUTION 1: Brute force/Using nested loop
# O(N^2) TIME AND O(1) SPACE
def maxArea1(height):
    result = 0

    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])
            result = max(result, area)
    return result


# SOLUTION 2: Using pointers
# O(N) TIME AND O(1) SPACE
def maxArea2(height):
    result = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        result = max(result, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return result
