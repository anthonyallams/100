import pytest
from easy.majorityelement import lengthOfLastWord


def test_lengthOfLastWord():
    s,s1,s2 = "Hello World","   fly me   to   the moon  ","luffy is still joyboy"
    assert lengthOfLastWord(s) == 5
    assert lengthOfLastWord(s1) == 4
    assert lengthOfLastWord(s2) == 6