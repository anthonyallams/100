import pytest
from medium.productofarrayexcept import productExceptSelf


def test_productofarrayexceptself():
    nums, nums1 = [1, 2, 3, 4], [-1, 1, 0, -3, 3]
    assert (productExceptSelf(nums)) == [24, 12, 8, 6]
    assert (productExceptSelf(nums1)) == [0, 0, 9, 0, 0]
