import pytest
from medium.twosum2 import twoSum1

def test_twoSum():
    numbers1, numbers2, numbers3 = [2,7,11,15], [2,3,4], [-1,0]
    target1, target2, target3 = 9, 6, -1
    assert(twoSum1(numbers1, target1)) == [1,2]
    assert(twoSum1(numbers2, target2)) == [1,3]
    assert(twoSum1(numbers3, target3)) == [1,2]