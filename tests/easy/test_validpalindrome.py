import pytest
from easy.validpalindrome import isPalindrome1, isPalindrome2


# To get the nums
def test_ispalindrome():
    s = "A man, a plan, a canal: Panama"
    y = "race a car"
    assert isPalindrome1(s) == True
    # breakpoint()
    assert isPalindrome2(s) == True
    assert isPalindrome1(y) == False
    assert isPalindrome2(y) == False
