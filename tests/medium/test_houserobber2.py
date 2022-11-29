import pytest
from medium.houserobber2 import rob

def test_houserobber2():
    nums, nums1 = [2,3,2],[1,2,3,1]
    assert(rob(nums)) == 3
    assert(rob(nums1)) == 4