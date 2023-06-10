"""
WORD PATTERN
https://leetcode.com/problems/word-pattern/
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


# SOLUTION 1: Using zip function and hashmap
# O(N) TIME AND O(N) SPACE
def wordPattern(pattern: str, s: str) -> bool:
    """
    Define a hashmap to store word-to-letter and letter-to-words
    Loop through the zipped values of words and pattern,
    checking if a word is in wordToLetter and has a value of letter and vice versa
    """
    words = s.split()
    if len(words) != len(pattern):
        return False

    wordToLetter = {}
    letterToWord = {}

    for letter, word in zip(pattern, words):
        if word in wordToLetter and wordToLetter[word] != letter:
            return False
        else:
            if letter in letterToWord and letterToWord[letter] != word:
                return False
        wordToLetter[word] = letter
        letterToWord[letter] = word

    return True
