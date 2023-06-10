"""
REVERSE BITS
https://leetcode.com/problems/reverse-bits/
Reverse bits of a given 32 bits unsigned integer.
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
so return 964176192 which its binary representation is 00111001011110000010100101000000.
"""


# SOLUTION 1: Using bit manipulation by left shifting the output and right shifting the input
# O(N) TIME AND O(1) SPACE
def reverseBits1(n):
    output = 0
    for _ in range(32):
        output <<= 1
        if n & 1:
            output += 1
        n >>= 1
    return output
