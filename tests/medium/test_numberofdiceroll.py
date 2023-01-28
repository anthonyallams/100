import pytest
from medium.numberofdiceroll import numRollsToTarget

def test_numberofdiceroll():
    n,k,target = 1,6,3
    assert(numRollsToTarget(n, k,target )) == 1


def test_numberofdiceroll1():
    n, k,target = 2,6,7
    assert(sorted(numRollsToTarget(n, k,target))) == 6

def test_numberofdiceroll2():
    n, k,target = 30,30,500 
    assert(sorted(numRollsToTarget(n, k,target))) == 222616187