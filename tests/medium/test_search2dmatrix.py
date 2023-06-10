import pytest
from medium.search2dmatrix import searchMatrix


def test_search2dmatrix():
    matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3
    assert (searchMatrix(matrix, target)) == True


def test_search2dmatrix1():
    matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13
    assert (searchMatrix(matrix, target)) == False
