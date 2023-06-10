"""
CHALLENGE: Sentence Reversal
Given a string of words, reverse all the words. Removing all leading and trailing whitespace

EXAMPLE: Given the following strings,  we would get:

reverse_sentence('This is the best') => 'best the is This'
reverse_sentence('  space here') =>'here space'
reverse_sentence('right hand space      ') =>'here space'
reverse_sentence('Hello Sir,  what can I get you? ') =>'here space'
"""


# SOLUTION 1: Splitting words into a list and reversing them
# O(N) TIME AND O(N) SPACE
def reverse1(sen):
    startOfword = 0
    words = []

    for idx in range(len(sen)):
        char = sen[idx]

        if char == " ":
            words.append(sen[startOfword:idx])
            startOfword = idx
        elif sen[startOfword] == " ":
            words.append(" ")
            startOfword = idx
    words.append(sen[startOfword:])
    reversed_words = reverseList(words)
    return "".join(reversed_words)


def reverseList(list):
    left, right = 0, len(list) - 1
    while left <= right:
        list[left], list[right] = list[right], list[left]
        left, right = left + 1, right - 1
    return list


# SOLUTION 2: Reverse the entire sentence and then reverse the individual words in the sentence list
# O(N) TIME AND O(N) SPACE
def reverse2(sen):
    chars = [char for char in sen]
    reverseListRange(chars, 0, len(sen) - 1)

    startOfword = 0
    while startOfword < len(chars):
        endOfword = startOfword
        while endOfword < len(chars) and chars[endOfword] != " ":
            endOfword += 1

        reverseListRange(chars, startOfword, endOfword - 1)
        startOfword = endOfword + 1

    return "".join(chars)


def reverseListRange(list, start, end):
    while start <= end:
        list[start], list[end] = list[end], list[start]
        start, end = start + 1, end - 1
    return list
