'''
CHALLENGE
Given two string arguments, check to see if they are anagrams of eachother. A string is an anagram of another if it uses the same characters in the same quantity. Only consider characters, not spaces or punctuation. Consider capital letters to be the same as lower case

EXAMPLE
anagrams('RAIL! SAFETY!','fairy tales') ==> True
anagrams('Hi there','Bye there') ==> False
anagrams('rail safety','fairy tales') ==> True
anagrams('Helllo there@','There Helllo!@##$$%%.') ==> False
anagrams('Helllo there@t','There Helllo!@##$$%%.') ==> True
'''

# SOLUTION 1: Sorting and Comparing the characters in sorted string
# Import regular expressions and test module
import re


def anagrams1(str1, str2):  # O(n)
    # Lower the string characters,
    # Pass the lowercase chars through a sort function(sorted)
    # Since sorted return a list, convert to string via join
    # Replace non-alphanumeric characters using re.sub()
    word1 = re.sub('[^\w]', '', ''.join(sorted(str1.lower())))
    word2 = re.sub('[^\w]', '', ''.join(sorted(str2.lower())))

    # Compare the length of word1 and word2
    if len(word1) != len(word2):
        return False

    # Loop through sorted string and compare the characters of str1 and str2
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            return False
    return True


# SOLUTION 2: Using hashmap to compare sorted string
def anagrams2(str1, str2):  # O(n)
    # Lower the string characters,
    # Pass the lowercase chars through a sort function(sorted)
    # Since sorted return a list, convert to string via join
    # Replace non-alphanumeric characters using re.sub()
    word1 = re.sub('[^\w]', '', ''.join(sorted(str1.lower())))
    word2 = re.sub('[^\w]', '', ''.join(sorted(str2.lower())))

    # Compare the length of both strings
    if len(word1) != len(word2):
        return False

    # Initialize hashmap
    counter = {}

    # Loop through the keys in counter dict
    # If a character in word1 exists, increment the value by 1, else add it
    for w in word1:
        if w in counter:
            counter[w] += 1
        else:
            counter[w] = 1

    # Loop through the keys in the hashmap
    # If a character in word2 exists, decrement the value by 1, else add it
    for w in word2:
        if w in counter:
            counter[w] -= 1
        else:
            counter[w] = 1

    # Now, loop through the hashmap
    # If any character(key) has a value other than 0, return false, else return True
    for key, value in counter.items():
        if value != 0:
            return False
    return True

anagrams1('Helllo there@', 'There Helllo!@##$$%%.')
