import pytest
from medium.encodedecode import encode, decode


def test_encode():
    strs, strs1 = ["lint", "code", "love", "you"], ["we", "say", ":", "yes"]
    encoded_str = encode(strs)
    encoded_str1 = encode(strs1)
    # breakpoint()
    assert (type(encoded_str)) == str
    assert (type(encoded_str1)) == str
    assert (encoded_str) != ["lint", "code", "love", "you"]
    assert (encoded_str1) != ["we", "say", ":", "yes"]


def test_decode():
    strs, strs1 = ["lint", "code", "love", "you"], ["we", "say", ":", "yes"]
    encoded_str = encode(strs)
    encoded_str1 = encode(strs1)
    assert (decode(encoded_str)) == ["lint", "code", "love", "you"]
    assert (decode(encoded_str1)) == ["we", "say", ":", "yes"]
