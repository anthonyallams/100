import pytest
from easy.longestcommonprefix import longestCommonPrefix

def test_longestCommonPrefix():
    strs,strs1 = ["flower","flow","flight"],["dog","racecar","car"]
    assert(longestCommonPrefix(strs)) == 'fl'
    assert(longestCommonPrefix(strs1)) == ''


