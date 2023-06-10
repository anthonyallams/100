import pytest
from easy.fibonacci import fibonacci1, fibonacci2, fibonacci3


def test_fibonacci():
    n1, n2, n3 = 10, 1, 12
    assert (fibonacci1(n1)) == 55
    assert (fibonacci1(n2)) == 1
    assert (fibonacci1(n3)) == 144
    assert (fibonacci2(n1)) == 55
    assert (fibonacci2(n2)) == 1
    assert (fibonacci2(n3)) == 144
    assert (fibonacci3(n1)) == 55
    assert (fibonacci3(n2)) == 1
    assert (fibonacci3(n3)) == 144
