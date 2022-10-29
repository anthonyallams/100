"""
PLUS ONE
https://leetcode.com/problems/plus-one/ 66

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.Increment the large integer by one and return the resulting array of digits.
"""
#SOLUTION 1: Using integer manipulation
#O(N) TIME AND 0(N) SPACE
def plusOne1(digits):
    digits = digits[::-1]
    carry, idx = 1, 0

    while carry:
        if idx < len(digits):
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                carry = 0
        else:
            digits.append(1)
            carry = 0
        idx += 1
    return digits[::-1]

#SOLUTION 2: Using inbuilt python methods
#O(N) TIME AND 0(N) SPACE
def plusOne2(digits):
    return [int(v) for v in str(int(''.join(map(str, digits)))+1)]