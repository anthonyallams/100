"""
PRIME NUMBER 
A prime no is a no that can only be divisible by 1 and itself
Given a number, check if it is a prime or not
"""


# SOLUTION ONE: Using optimized iterative approach to check
# O(SQRT(N)) TIME AND O(1) SPACE
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
