import pytest
from easy.countingbits import countingBits1

def test_countingbits():
    n, n1 = 2,5
    assert(countingBits1(n1)) == [0, 1, 1, 2, 1, 2]
    assert(countingBits1(n)) == [0, 1, 1, 2, 1, 2]