"""
CAESAR CIPHER ENCRYPTOR
Given a lowercase, non-empty string and an integer key, return the modified string shifted key times
"""
#SOLUTION 1: Using python's unicode characters with a =>97 and z => 122
#O(N) TIME AND O(N) SPACE
def cipher1(st, key):
    values = []
    newkey = key % 26

    for s in st:
        num = ord(s) + newkey
        values.append(chr(num) if num <= 122 else chr(96 + num % 122))
    return "".join(values)

#SOLUTION 2: Using alphabetical values rather than unicode characters
def cipher2(st, key):
    values = []
    newkey = key % 26
    alphabets = list('abcdefghijklmnopqrstuvwxyz')

    for s in st:
        num = alphabets.index(s) + newkey
        values.append(alphabets[num] if num <=25 else alphabets[-1 + num % 25])
    return "".join(values)