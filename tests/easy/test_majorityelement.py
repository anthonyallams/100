import pytest
from easy.majorityelement import majorityElement,majorityElement1


def test_majorityElement():
    nums, nums1 = [3,2,3], [2,2,1,1,1,2,2]
    assert majorityElement(nums) == 3
    assert majorityElement(nums1) == 2
    assert majorityElement1(nums) == 3
    assert majorityElement1(nums1) == 2