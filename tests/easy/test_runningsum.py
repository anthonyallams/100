import pytest
from easy.runningsum import runningSum, runningSum1, runningSum2


def test_runningsum():
    nums = [1, 2, 3, 4]  # [1,3,6,10]
    nums1 = [1, 1, 1, 1, 1]  # [1,2,3,4,5]
    nums2 = [3, 1, 2, 10, 1]  # [3,4,6,16,17]
    assert runningSum(nums) == [1, 3, 6, 10]
    assert runningSum(nums1) == [1, 2, 3, 4, 5]
    assert runningSum1([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert runningSum1([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert runningSum2([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert runningSum2([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
