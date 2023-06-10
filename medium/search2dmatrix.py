"""
18TH JANUARY 2023 (MEDIUM)
SEARCH A 2D MATRIX
https://leetcode.com/problems/search-a-2d-matrix/solutions/
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""


# Using Binary search
# O(LOGN) TIME AND O(1) SPACE
def searchMatrix(matrix: list[list[int]], target: int):
    """ """
    row1, col1 = len(matrix), len(matrix[0])
    left, right = 0, row1 * col1

    while left < right:
        mid = (left + right) // 2
        row = mid // col1
        col = mid % col1
        num = matrix[row][col]
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid
    return False
