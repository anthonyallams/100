import pytest
from easy.maximumsubarray import maxSubArray1, maxSubArray2

def test_maxSubArray():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert maxSubArray1(nums) == 6
    assert maxSubArray2(nums) == 6