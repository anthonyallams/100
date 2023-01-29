import pytest
from easy.ransomenote import canConstruct

def test_ransomenote_1():
    ransomNote, magazine =  "a","b" #false
    assert(canConstruct(ransomNote,magazine)) == False


def test_ransomenote_2():
    ransomNote, magazine = "aa","ab" #false
    assert(canConstruct(ransomNote,magazine)) == False

def test_ransomenote_3():
    ransomNote, magazine = "aa", "aab" #true
    assert(canConstruct(ransomNote,magazine)) == True