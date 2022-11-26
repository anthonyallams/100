import pytest
from medium.houserobber import rob

def test_houserobber():
    nums, nums1 = [1,2,3,1],[2,7,9,3,1]
    assert(rob(nums)) == 4
    assert(rob(nums1)) == 12
    