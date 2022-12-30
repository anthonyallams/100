import pytest
from medium.sortcolors import sortColors


def test_sortcolors():
    nums,nums1 = [2,0,2,1,1,0],[2,0,1] #[0,0,1,1,2,2],[0,1,2]
    assert sortColors(nums) == [0,0,1,1,2,2]
    assert sortColors(nums1) == [0,1,2]