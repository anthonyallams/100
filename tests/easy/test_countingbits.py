import pytest
from easy.countingbits import countBits1, countBits2


def test_countingbits():
    n, n1 = 2, 5
    assert (countBits1(n1)) == [0, 1, 1, 2, 1, 2]
    assert (countBits1(n)) == [0, 1, 1]
    assert (countBits2(n1)) == [0, 1, 1, 2, 1, 2]
    assert (countBits2(n)) == [0, 1, 1]
