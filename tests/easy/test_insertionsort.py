import pytest
from easy.insertionsort import insertion_sort1


def test_insertionsort():
    num1, num2 = [8, 5, 2, 9, 5, 6, 3], [9, 6, 4, 2, 3, 5, 7, 0, 1]
    assert (insertion_sort1(num1)) == [2, 3, 5, 5, 6, 8, 9]
    assert (insertion_sort1(num2)) == [0, 1, 2, 3, 4, 5, 6, 7, 9]
