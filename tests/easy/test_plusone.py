import pytest
from easy.plusone import plusOne1, plusOne2


def test_plusone():
    digits = [1, 2, 3]
    digits1 = [2, 9, 2, 9, 9]
    assert (plusOne1(digits)) == [1, 2, 4]
    assert (plusOne2(digits)) == [1, 2, 4]
    assert (plusOne1(digits1)) == [2, 9, 3, 0, 0]
    assert (plusOne2(digits1)) == [2, 9, 3, 0, 0]
