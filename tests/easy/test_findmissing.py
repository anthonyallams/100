import pytest
from easy.findmissing import finder1, finder2

def test_topKFrequent():
    nums1, nums2 =[1,2,3,4,5,6,7],[3,7,2,1,4,6]
    nums3, nums4 =[2,4,6,8,10,12],[2,6,8,10,12]
    nums5, nums6 =[1,2,3,4,10,11,12],[1,2,4,10,11,12]
    
    assert(finder1(nums1, nums2)) == 5
    assert(finder1(nums3, nums4)) == 4
    assert(finder1(nums5, nums6)) == 3
    assert(finder2(nums1, nums2)) == 5
    assert(finder2(nums3, nums4)) == 4
    assert(finder2(nums5, nums6)) == 3