import pytest
from easy.besttimetobuy import maxProfit,maxProfit1

def test_besttimetobuy():
    prices, prices1 = [7,1,5,3,6,4], [7,6,4,3,1] #5,0
    assert(maxProfit(prices)) == 5
    assert(maxProfit(prices1)) == 0

def test_besttimetobuy1():
    prices, prices1 = [7,1,5,3,6,4], [7,6,4,3,1] #5,0
    assert(maxProfit1(prices)) == 5
    assert(maxProfit1(prices1)) == 0