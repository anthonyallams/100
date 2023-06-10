import pytest
from easy.finddisappearednumbers import findDisappearedNumbers, findDisappearedNumbers1


def test_findDisappearedNumbers():
    # nums, nums1 = [1,1],[4,3,2,7,8,2,3,1]
    assert findDisappearedNumbers([1, 1]) == [2]
    assert findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert findDisappearedNumbers1([1, 1]) == [2]
    assert findDisappearedNumbers1([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
