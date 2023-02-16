import pytest
from medium.maximumicecreambars import maxIceCream, maxIceCream2

def test_maximumicecreambars_1():
    costs, coins  = [1,3,2,4,1], 7
    assert(maxIceCream(costs, coins)) == 4
    assert(maxIceCream2(costs, coins)) == 4


def test_maximumicecreambars_2():
    costs, coins = [10,6,8,7,7,8], 5
    assert(maxIceCream(costs, coins)) == 0
    assert(maxIceCream2(costs, coins)) == 0


def test_maximumicecreambars_3():
    costs, coins = [1,6,3,1,2,5], 20
    assert(maxIceCream(costs, coins)) == 6
    assert(maxIceCream2(costs, coins)) == 6