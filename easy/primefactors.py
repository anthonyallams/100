'''
CHALLENGE: FIND PRIME FACTORS OF A NUMBER
Given a non-negative integer, find the prime factors
NB: prime factorization or integer factorization of a number is breaking a number down into the set of prime numbers which multiply together to result in the original number.
A prime number is a whole number greater than 1 that can not be made by multiplying other whole numbers
The first few prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23 etc

EXAMPLE
Given the following array, the prime factors are given.
prime_factors(17) => [17]
prime_factors(84) => [2,2,3,7]
prime_factors(48) => [2,2,2,2,3]
prime_factors(147) => [3,7,7]
prime_factors(330) =>[2,3,5,11]
prime_factors(1318) =>[2,659]
'''


# SOLUTION 1: Brute force approach: For loop
import math


def prime_factors1(num):  # O(n^2)
    # Initialize the list for storing the prime factors.
    prime_factors = []

    # Prime numbers are usually between 2 and the square root of the number, or a value more than the square root which is also prime number. Also prime numbers divide prime factors without remainder
    # Since 2 is the first prime number, start looping from 2 to sqrt root and record each range value
    # Then divide number with value in the range
    for el in range(2, int(math.sqrt(num)+1)):
        while num % el == 0:
            prime_factors.append(el)
            num /= el

    if num > 1:
        prime_factors.append(num)
    return prime_factors

# SOLUTION 2: Brute force: Using while loop - Similar to Solution 1, aside from use of while loop


def prime_factors2(num):
    prime_factors = []
    prime_num = 2

    while prime_num <= int(math.sqrt(num)):
        while num % prime_num == 0:
            prime_factors.append(prime_num)
            num /= prime_num
        prime_num += 1

    if num > 2:
        prime_factors.append(num)
    return prime_factors
    # print(prime_factors(17))
    # print(prime_factors(48))  # => [2,2,2,2,3]

    # Test class function

# SOLUTION 3: Optimized solution using loop


def prime_factors3(num):
    # Initialize the list for storing prime factors
    prime_factors = []

    # Since 2 is the first prime number, divide the num as long as no remainder and append
    while num % 2 == 0:
        prime_factors.append(2)
        num /= 2

    # Start looping from 3 with step of 2, repeat the previous steps
    for el in range(3, int(math.sqrt(num))+1, 2):
        while num % el == 0:
            prime_factors.append(int(el))
            num /= el

    if num > 2:
        prime_factors.append(num)
    return prime_factors

