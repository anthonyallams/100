import pytest
from easy.valid_anagram import isAnagram1, isAnagram2, isAnagram3,isAnagram4

def test_anagram_true():
    s,t = "anagram","nagaram"
    assert(isAnagram1(s, t))== True
    assert(isAnagram2(s, t))== True
    assert(isAnagram3(s, t))== True

def test_anagram_false():
    s,t = "rat", "car"
    assert(isAnagram1(s,t))==False
    assert(isAnagram2(s,t))==False
    assert(isAnagram3(s,t))==False

def test_anagram_sentence():
    s, t = 'Helllo there@', 'There Helllo!@##$$%%.'
    assert(isAnagram4(s,t))==True