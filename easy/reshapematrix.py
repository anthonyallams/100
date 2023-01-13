"""
RESHAPE THE MATRIX
https://leetcode.com/problems/reshape-the-matrix/
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one 
with a different size r x c keeping its original data.You are given an m x n matrix mat and two integers r and c 
representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""
#SOLUTION 1: Iterative approach
#O(N.M) TIME AND O(N) SPACE
def matrixReshape(mat:list[int],r:int,c:int)->list[list[int]]:
    """
    Get the row and col dimensions of mat. 
    Check if the contents of mat can go into the new matrix
    Define a new matrix based on r & c and 
    Initialize nums to keep track of elemnts added to new matrix
    Loop through rows & cols of mat and set the row and col we are writing into the new matrix
    Add the elements from mat into the row/col of new matrix(result) and return
    """
    r1 = len(mat)
    c1 = len(mat[0])

    if r1*c1 != r*c:
        return mat
    
    result = [[0 for _ in range(c)]for _ in range(r)]
    nums = 0

    for i in range(r1):
        for j in range(c1):
            row = nums//c
            col = nums%c
            result[row][col] = mat[i][j]
            nums += 1
    return result
