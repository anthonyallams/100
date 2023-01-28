import pytest
from easy.randsomenote import canConstruct

def test_randsomenote_1():
    ransomNote, magazine =  "a","b" #false
    assert(canConstruct(ransomNote,magazine)) == False


def test_randsomenote_2():
    ransomNote, magazine = "aa","ab" #false
    assert(canConstruct(ransomNote,magazine)) == False

def test_randsomenote_3():
    ransomNote, magazine = "aa", "aab" #true
    assert(canConstruct(ransomNote,magazine)) == False