"""
ENCODE AND DECODE STRINGS
https://leetcode.com/problems/encode-and-decode-strings/
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings. Please implement encode and decode

Example1
Input: ["lint","code","love","you"] Output: ["lint","code","love","you"] 
Explanation: One possible encode method is: "lint:;code:;love:;you"

Example2
Input: ["we", "say", ":", "yes"] Output: ["we", "say", ":", "yes"] 
Explanation: One possible encode method is: "we:;say:;:::;yes”

Note:
The string may contain any possible characters out of 256 valid ascii characters. 
Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
"""


# SOLUTION 1: Encode the string using len of str and "#" character
# O(N) TIME AND O(N) SPACE
def encode(strs: list[str]) -> str:
    """
    Initialize and empty string result
    For each str in strs, get the len of str and append the length + "#" + str to the result
    """
    result = ""
    for st in strs:
        result += str(len(st)) + "#" + st
    return result


def decode(strs: str) -> list[str]:
    """
    Initialize index to track both elements in strs and elements in each strs string, and a list
    For every element in the list, extract the length and using the length + #, get the element
    Append the element to the result list and increment the indexes used
    """
    i, result = 0, []

    while i < len(strs):
        j = i
        while strs[j] != "#":
            j += 1
        length = int(strs[i:j])
        result.append(strs[j + 1 : j + 1 + length])
        i = j + 1 + length

    return result
