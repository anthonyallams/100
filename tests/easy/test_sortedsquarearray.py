import pytest
from easy.sortedsquarearray import sortedArray1, sortedArray2

def test_sortedArray():
    arr,arr1,arr2 = [1,2,3,5,6,8,9],[-4,1,2], [-7,-5,-4,3,6,8,9]
    assert(sortedArray1(arr)) == [1, 4, 9, 25, 36, 64, 81]
    assert(sortedArray1(arr1)) == [1, 4, 16]
    assert(sortedArray1(arr2)) == [9, 16, 25, 36, 49, 64, 81]
    assert(sortedArray2(arr)) == [1, 4, 9, 25, 36, 64, 81]
    assert(sortedArray2(arr1)) == [1, 4, 16]
    assert(sortedArray2(arr2)) == [9, 16, 25, 36, 49, 64, 81]