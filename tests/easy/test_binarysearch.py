import pytest
from easy.binarysearch import binarysearch


#To get the nums
def test_binarysearch():
    nums = [1,4,-6,9,-1,10,12,18]
    nums1 = [2,7,11,15]
    target = 12
    target1 = 9
    assert binarysearch(nums, target) == 6
    assert binarysearch(nums1, target) == -1
    assert binarysearch(nums1, target1) == -1
