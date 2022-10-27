import pytest
from easy.reverseword import reverse1, reverse2,reverse3


#To get the nums
def test_reverseword():
    st = ['a','l','l','a','m','s']
    st2 = ['h','e','l','l','o']
    assert reverse1(st) == None or ['s', 'm', 'a', 'l', 'l', 'a']
    # breakpoint()
    assert reverse2(st) == None or ['s', 'm', 'a', 'l', 'l', 'a']
    # breakpoint()
    assert reverse3(st) == None or ['s', 'm', 'a', 'l', 'l', 'a']
    assert reverse1(st2) == None or ['o', 'l', 'l', 'e', 'h']
    assert reverse2(st2) == None or ['o', 'l', 'l', 'e', 'h']
    assert reverse3(st2) == None or ['o', 'l', 'l', 'e', 'h']