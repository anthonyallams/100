import pytest
from easy.binarysearch import ispalindrome1, ispalindrome2, ispalindrome3


#To get the nums
def test_ispalindrome():
    s = "A man, a plan, a canal: Panama"
    y = "race a car"
    assert ispalindrome1(s) == True
    assert ispalindrome2(s) == True
    assert ispalindrome3(s) == True
    assert ispalindrome1(y) == False
    assert ispalindrome2(y) == False
    assert ispalindrome3(y) == False