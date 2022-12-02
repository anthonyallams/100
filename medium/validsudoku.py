"""
VALID SUDOKU
https://leetcode.com/problems/valid-sudoku/
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""
#SOLUTION 1: Using iterative approach and set to get and compare elements in rows, cols and squares
#O(N^2) TIME AND O(N^2) SPACE WHERE N = 9 rows/cols
from collections import defaultdict

def isValidSudoku(board):
  """
  Use defaultdict to get init rows, cols and grid square
  Use integer division of rows and columns (r//3, c//3) to get the unique grid square
  Loop through the rows and cols and check if elem is in rows, cols or grid; if yes, then Sudoku is not valid
  If element is not in rows, cols or grid; then add the elem to the row, col or grid and return True
  """
  rows = defaultdict(set)
  cols = defaultdict(set)
  grids = defaultdict(set)

  for r in range(9):
    for c in range(9):
        if board[r][c] == ".":
            continue

        if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grids[(r//3, c//3)]):
            return False
        
        rows[r].add(board[r][c])
        cols[c].add(board[r][c])
        grids[(r//3, c//3)].add(board[r][c])

  return True
