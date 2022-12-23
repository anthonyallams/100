import pytest
from easy.maximumnoballoon import maxNumberOfBalloons


def test_maximumnoballon():
    text, text1, text2 = "nlaebolko","loonbalxballpoon","leetcode" #1,2,0
    assert maxNumberOfBalloons(text) == 1
    assert maxNumberOfBalloons(text1) == 2
    assert maxNumberOfBalloons(text2) == 0
