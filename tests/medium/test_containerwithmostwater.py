import pytest
from medium.containerwithmostwater import maxArea1, maxArea2


def test_containerwithmostwater():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height1 = [1, 1]
    assert (maxArea1(height)) == 49
    assert (maxArea2(height)) == 49
    assert (maxArea1(height1)) == 1
    assert (maxArea2(height1)) == 1
