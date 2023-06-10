import pytest
from easy.missingnumber import missingNumber1, missingNumber2, missingNumber3


def test_countingbits():
    nums, nums1 = [3, 0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1]
    assert (missingNumber1(nums)) == 2
    assert (missingNumber1(nums1)) == 8
    assert (missingNumber2(nums)) == 2
    assert (missingNumber2(nums1)) == 8
    assert (missingNumber3(nums)) == 2
    assert (missingNumber3(nums1)) == 8
