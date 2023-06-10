import pytest
from easy.removeElement import removeElement, removeElement1, removeElement2


def test_removeElement():
    nums, val = [3, 2, 2, 3], 3  # [2,2,_,_]
    nums1, val1 = [0, 1, 2, 2, 3, 0, 4, 2], 2  # [0,1,4,0,3,_,_,_]
    assert removeElement(nums, val) == 2
    assert removeElement(nums1, val1) == 5
    assert removeElement1([3, 2, 2, 3], val) == 2
    assert removeElement1([0, 1, 2, 2, 3, 0, 4, 2], val1) == 5
    assert removeElement2([3, 2, 2, 3], val) == 2
    assert removeElement2([0, 1, 2, 2, 3, 0, 4, 2], val1) == 5
