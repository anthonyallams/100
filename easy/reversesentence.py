'''
CHALLENGE: Sentence Reversal
Given a string of words, reverse all the words. Removing all leading and trailing whitespace

EXAMPLE: Given the following strings,  we would get:

reverse_sentence('This is the best') => 'best the is This'
reverse_sentence('  space here') =>'here space'
reverse_sentence('right hand space      ') =>'here space'
reverse_sentence('Hello Sir,  what can I get you? ') =>'here space'
'''
from nose.tools import assert_equal

# SOLUTION 1: Using simple python methods to split and reverse


def reverse_sentence1(sen):
    # Check if the length of sentence is greater than 1
    if len(sen) <= 1:
        return sen

    # Split, reverse and join back the sentence words with space
    return ' '.join(reversed(sen.split()))


# SOLUTION 2: Using simple python array split, slice and reverse
def reverse_sentence2(sen):
    # Check if the length of sentence is greater than 1
    if len(sen) <= 1:
        return sen

    # Splice and reverse and join words back together
    return ' '.join(sen.split()[::-1])


# SOLUTION 3: Manually splitting the characters and words using a while loop
def reverse_sentence3(sen):
    # Check if the length of sentence is greater than 1
    if len(sen) <= 1:
        return sen

    # Initialize words array for storing the words, length and spaces
    words = []
    spaces = [' ']
    length = len(sen)

    # Tracker for indexing characters and words in the sentence
    i = 0

    # Loop through the entire sentences if tracker is less than sentence length
    while i < length:
        # If character is not a space
        if sen[i] not in spaces:
            # Beginning of a word in the sentence
            word_start = i
            # Loop through the individual words in the sentence if not space
            while i < length and sen[i] not in spaces:
                # Get tracker of word ending
                i += 1
            # Add words to the words array
            words.append(sen[word_start:i])
        i += 1
    return ' '.join(reversed(words))

    # Test class function


class TestReverseSentence(object):

    def test(self, solution):
        assert_equal(solution('This is the best'), 'best the is This')
        assert_equal(solution('Hello Sir,  what can I get you? '),
                     'you? get I can what Sir, Hello')
        assert_equal(solution('right hand space      '), 'space hand right')
        assert_equal(solution('    left hand space'), 'space hand left')
        print('All test cases passed')


# Run tests
t = TestReverseSentence()
t.test(reverse_sentence3)
