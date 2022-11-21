import pytest
from easy.mergesortedarray import merge

def test_mergesortedarray():
    nums1, m, nums2, n  = [1,2,3,0,0,0], 3, [2,5,6], 3
    assert(merge(nums1, m, nums2, n)) == [1,2, 2, 3, 5, 6]
