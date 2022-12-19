import pytest
from easy.isomorphicstring import isIsomorphic


def test_isomorphicstring():
    s,t = "egg", "add" #true
    s1,t1 = "paper", "title"#true
    s2,t2 = "foo", "bar"#false
    assert isIsomorphic(s,t) == True
    assert isIsomorphic(s1,t1) == True
    assert isIsomorphic(s2,t2) == False