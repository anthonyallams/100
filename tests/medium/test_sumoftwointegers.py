import pytest
from medium.sumoftwointegers import getSum


def test_sumoftwointegers():
    a,b = 1, 2 #3
    a1,b1 = 2, 3 #5
    assert getSum(a, b) == 3
    assert getSum(a1,b1) == 5
