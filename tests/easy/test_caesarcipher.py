import pytest
from easy.caesarcipher import cipher1, cipher2


def test_caesarcipher():
    st = "xyz"  #'zab'
    st2 = "cde"  #'hij'
    key = 2
    key2 = 5
    assert (cipher1(st, key)) == "zab"
    assert (cipher1(st2, key2)) == "hij"
    assert (cipher2(st, key)) == "zab"
    assert (cipher2(st2, key2)) == "hij"
