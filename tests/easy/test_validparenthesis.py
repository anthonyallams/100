import pytest
from easy.validparenthesis import isValid1


def test_isValid():
    s, s1, s2 = "(]", "()[]{}", "()"
    assert (isValid1(s)) == False
    assert (isValid1(s1)) == True
    assert (isValid1(s2)) == True
    # assert(isValid2(s)) == False
    # assert(isValid2(s1)) == True
    # assert(isValid2(s2)) == True
