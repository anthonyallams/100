import pytest
from easy.intersectionoftwoarray import intersect, intersect1


def test_intersectionoftwoarray():
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    assert (intersect(nums1, nums2)) == [2, 2]
    assert (intersect1(nums1, nums2)) == [2, 2]


def test_intersectionoftwoarray1():
    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    assert (sorted(intersect(nums1, nums2))) == [4, 9]
    assert (sorted(intersect1(nums1, nums2))) == [4, 9]
