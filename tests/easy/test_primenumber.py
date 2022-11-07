import pytest
from easy.primenumber import isPrime

def test_primenumbers():
    n,n1,n2= 10,11,23
    assert(isPrime(n)) == False
    assert(isPrime(n1)) == True
    assert(isPrime(n2)) == True