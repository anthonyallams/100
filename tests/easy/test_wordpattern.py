import pytest
from easy.wordpattern import wordPattern

def test_wordpattern_1():
    pattern,s = "abba","dog cat cat dog"
    assert(wordPattern(pattern,s )) == True


def test_wordpattern_2():
    pattern,s = "abba",  "dog cat cat fish"
    assert(wordPattern(pattern,s)) == False

def test_wordpattern_3():
    pattern, s = "aaaa", "dog cat cat dog"
    assert(wordPattern(pattern,s)) == False