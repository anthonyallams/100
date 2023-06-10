import pytest
from medium.topkfrequentelements import topKFrequent


def test_topKFrequent():
    nums, k = [1, 1, 1, 2, 2, 3], 2
    nums1, k1 = [1], 1
    nums2, k2 = [2, 2, 4, 5, 6, 6], 2
    assert (topKFrequent(nums, k)) == [1, 2]
    assert (topKFrequent(nums1, k1)) == [1]
    assert (topKFrequent(nums2, k2)) == [2, 6]
