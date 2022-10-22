import pytest
from easy.palindromenumber import isPalindrome1, isPalindrome2, isPalindrome3


#To get the nums
def test_ispalindrome():
    x = 1332231
    y = 121
    assert isPalindrome1(x) == False
    assert isPalindrome2(x) == False
    assert isPalindrome3(x) == False
    assert isPalindrome1(y) == True
    assert isPalindrome2(y) == True
    assert isPalindrome3(y) == True
