import pytest
from medium.groupanagrams import groupAnagrams1, groupAnagrams2


def test_groupAnagrams():
    strs1, strs2, strs3 = [""], ["a"], ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert (groupAnagrams1(strs1)) == [[""]]
    # breakpoint()
    assert (groupAnagrams1(strs2)) == [["a"]]
    assert (groupAnagrams1(strs3)) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert (groupAnagrams2(strs1)) == [[""]]
    assert (groupAnagrams2(strs2)) == [["a"]]
    assert (groupAnagrams2(strs3)) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
