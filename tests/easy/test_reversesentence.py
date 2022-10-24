import pytest
from easy.reverseword import reverse1, reverse2


#To get the nums
def test_reverseword():
    sentence = 'This is the best'
    sentence2 = 'Hello Sir,  what can I get you? '
    assert reverse1(sentence) == 'best the is This'
    assert reverse2(sentence) == 'best the is This'
    assert reverse1(sentence2) == 'you? get I can what Sir, Hello'
    assert reverse2(sentence2) == 'you? get I can what Sir, Hello'