import pytest
from easy.replaceelementwithgreatestelement import replaceElements


def test_replaceElements():
    arr,arr1 = [17,18,5,4,6,1],[400]
    assert replaceElements(arr) == [18,6,6,6,1,-1]
    assert replaceElements(arr1) == [-1]
