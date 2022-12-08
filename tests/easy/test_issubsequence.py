import pytest
from easy.majorityelement import isSubsequence


def test_isSubsequence():
    s,t = "abc", "ahbgdc"
    s1,t1 = "axc", "ahbgdc"
    assert isSubsequence(s, t) == True
    assert isSubsequence(s1, t1) == False

