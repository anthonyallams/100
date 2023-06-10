import pytest
from easy.climbingstairs import climbStairs1, climbStairs2, climbStairs3


def test_climbingstairs():
    n1, n2, n3 = 2, 5, 10
    assert (climbStairs1(n1)) == 2
    assert (climbStairs1(n2)) == 8
    assert (climbStairs1(n3)) == 89
    assert (climbStairs2(n1)) == 2
    assert (climbStairs2(n2)) == 8
    assert (climbStairs2(n3)) == 89
    assert (climbStairs3(n1)) == 2
    assert (climbStairs3(n2)) == 8
    assert (climbStairs3(n3)) == 89
