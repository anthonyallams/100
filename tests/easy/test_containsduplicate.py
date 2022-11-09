import pytest
from easy.containsduplicate import containsduplicate1, containsduplicate2

def test_containsduplicate():
    nums,nums1,nums2 = [1,2,3,1],[1,2,3,4], [1,1,1,3,3,4,3,2,4,2]
    assert(containsduplicate1(nums)) == True
    assert(containsduplicate1(nums1)) == False
    assert(containsduplicate1(nums2)) == True
    assert(containsduplicate2(nums)) == True
    assert(containsduplicate2(nums1)) == False
    assert(containsduplicate2(nums2)) == True