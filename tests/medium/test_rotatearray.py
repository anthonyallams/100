import pytest
from medium.rotatearray import rotate,rotate1,rotate2


def test_rotatearray():
    nums,k = [1,2,3,4,5,6,7],3 #[5,6,7,1,2,3,4]
    nums1,k1 = [-1,-100,3,99],2#[3,99,-1,-100]
    assert rotate(nums, k) == [5,6,7,1,2,3,4]
    assert rotate(nums1, k1) == [3,99,-1,-100]
    assert rotate1([1,2,3,4,5,6,7],k) == [5,6,7,1,2,3,4]
    assert rotate1([-1,-100,3,99], k1) == [3,99,-1,-100]
    assert rotate2([1,2,3,4,5,6,7],k) == [5,6,7,1,2,3,4]
    assert rotate2([-1,-100,3,99], k1) == [3,99,-1,-100]