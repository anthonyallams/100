import pytest
from easy.detectcapital import detectCapitalUse


def test_detectcapital_1():
    word = "USA"
    assert (detectCapitalUse(word)) == True


def test_detectcapital_2():
    word = "fLaG"
    assert (detectCapitalUse(word)) == False


def test_detectcapital_3():
    word = "leetcode"
    assert (detectCapitalUse(word)) == True
