import pytest
from medium.encodedecode import encode, decode

def test_encodedecode():
    strs,strs1 = ["lint","code","love","you"], ["we", "say", ":", "yes"]
    encoded_str = encode(strs)
    encoded_str1 = encode(strs1)
    assert(encoded_str) != ["lint","code","love","you"]
    assert(encoded_str1) != ["we", "say", ":", "yes"]
    assert(decode(encoded_str)) == ["lint","code","love","you"]
    assert(decode(encoded_str1)) == ["we", "say", ":", "yes"]
