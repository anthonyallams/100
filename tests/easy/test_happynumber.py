import pytest
from easy.happynumber import isHappy


def test_countingbits():
    nums, nums1 = 19, 2
    assert (isHappy(nums)) == True
    assert (isHappy(nums1)) == False
