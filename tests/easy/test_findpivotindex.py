import pytest
from easy.findpivotindex import pivotIndex, pivotIndex1, pivotIndex2


def test_findpivotindex():
    nums, nums1, nums2 = [1, 7, 3, 6, 5, 6], [1, 2, 3], [2, 1, -1]  # 3,-1,0
    assert pivotIndex(nums) == 3
    assert pivotIndex(nums1) == -1
    assert pivotIndex(nums2) == 0
    assert pivotIndex1(nums) == 3
    assert pivotIndex1(nums1) == -1
    assert pivotIndex1(nums2) == 0
    assert pivotIndex2(nums) == 3
    assert pivotIndex2(nums1) == -1
    assert pivotIndex2(nums2) == 0
