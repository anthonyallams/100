"""
PASCAL'S TRIANGLE
https://leetcode.com/problems/pascals-triangle/
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown;

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
"""
#SOLUTION 1: Using nested loop to calculate the elements and append it
#O(N^2) TIME AND O(N) SPACE
def generate(numRows:int) -> list[list[int]]:
    """
    Initialize result variable for the first number in pascal triangle, 1
    Loop through the numRows, create a temp var to append 0 to the begining and end of first number
    Loop through len of last element in result, add subsequent elements to row and append it to the result
    """
    res = [[1]]
    for _ in range(numRows-1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1])+1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res

