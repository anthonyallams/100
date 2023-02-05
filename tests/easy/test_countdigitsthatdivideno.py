import pytest
from easy.countdigitsthatdivideno import countDigits

def test_countdigitsthatdivideno_1():
    num = 7
    assert(countDigits(num)) == 1


def test_countdigitsthatdivideno_2():
    num = 121
    assert(countDigits(num)) == 2


def test_countdigitsthatdivideno_3():
    num = 1248
    assert(countDigits(num)) == 4