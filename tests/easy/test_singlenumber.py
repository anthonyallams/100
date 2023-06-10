import pytest
from easy.singlenumber import singleNumber1, singleNumber2


def test_reverseword():
    nums = [4, 1, 2, 1, 2]
    nums2 = [2, 7, 10, 2, 7]
    assert singleNumber1(nums) == 4
    assert singleNumber1(nums2) == 10
    assert singleNumber2(nums) == 4
    assert singleNumber2(nums2) == 10
