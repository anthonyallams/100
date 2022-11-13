import pytest
from easy.reversebits import reverseBits1#,reverseBits2

def test_countingbits():
    n = 11111111111111111111111111111101
    assert(reverseBits1(n)) == 3180214499
    # assert(reverseBits2(n)) == 3180214499