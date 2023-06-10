import pytest
from easy.twosum import twoSum1, twoSum2, twoSum3, twoSum4


# To get the nums
def test_twoSum_nums():
    nums = [2, 7, 11, 15]
    nums1 = [1, 4, -6, 9, -1, 10, 12, 18]
    target = 9
    target1 = 12
    assert twoSum1(nums, target) == [2, 7]
    assert twoSum2(nums, target) == [2, 7]
    assert twoSum3(nums, target) == [2, 7]
    assert twoSum1(nums1, target1) == [-6, 18]
    assert twoSum2(nums1, target1) == [-6, 18]
    assert twoSum3(nums1, target1) == [-6, 18]


# To get the indices
def test_twoSum_indices():
    nums = [2, 7, 11, 15]
    nums1 = [1, 4, -6, 9, -1, 10, 12, 18]
    target = 12
    target2 = 9
    assert twoSum4(nums, target2) == [0, 1]
    assert twoSum4(nums1, target) == [2, 7]
