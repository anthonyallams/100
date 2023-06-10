import pytest
from easy.movezeroes import moveZeroes


def test_movezeroes():
    nums = [0, 1, 0, 3, 12]
    assert (moveZeroes(nums)) == [1, 3, 12, 0, 0]
