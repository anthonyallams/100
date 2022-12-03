import pytest
from medium.longestconsecutivesequence import longestConsecutive

def test_longestconsecutivesubarray():
    nums, nums1 = [100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1]
    assert(longestConsecutive(nums)) == 4
    assert(longestConsecutive(nums1)) == 9