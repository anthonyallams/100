import pytest
from medium.threesum import threeSum1


def test_threesum():
    num1, num2, num3 = [0, 1, 1], [-1, 0, 1, 2, -1, -4], [-8, -6, 1, 2, 3, 5, 6, 12]
    assert (threeSum1(num1)) == []
    assert (threeSum1(num2)) == [[-1, -1, 2], [-1, 0, 1]]
    assert (threeSum1(num3)) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    # assert(threeSum2(num1)) == []
    # assert(threeSum2(num2)) == [[-1,-1,2],[-1,0,1]]
    # assert(threeSum2(num3)) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
