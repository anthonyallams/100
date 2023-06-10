"""
CHALLENGE: FIND MISSING ELEMENT IN AN ARRAY
Given an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

EXAMPLE
Given the following array, the first array is shuffled and the following numbers are removed.
finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]) => 5
finder([2,4,6,8,10,12],[2,6,8,10,12]) => 4
finder([1,2,3,4,10,11,12],[1,2,4,10,11,12]) =>3
"""


# SOLUTION 1: Subtracting the sum of arr2 from arr1
# O(N) TIME AND O(1)
def finder1(arr1, arr2):
    return sum(arr1) - sum(arr2)


# SOLUTION 2: Using hashmap
# O(N) TIME AND O(N) SPACE
def finder2(arr1, arr2):
    hashmap = {}

    for arr in arr1:
        hashmap[arr] = 1 + hashmap.get(arr, 0)

    for el in hashmap:
        if el not in arr2:
            return el


# # SOLUTION 1: Using hashmap to store repetitions. Not optimal for duplicates


# def finder1(arr1, arr2):  # O(n)
#     # Check if there are elements in the array
#     if len(arr1) < 1 or len(arr2) < 1:
#         return None

#     # Initialize the hashmap for storing count of values
#     counter = {}

#     # Since arr2 was shuffled from arr1, it has less no of elements
#     # Initialize every key to value of 1 if it is not already in the dictionary
#     for el in arr2:
#         if el not in counter:
#             counter[el] = 1

#     # If key is already in dictionary, subtract 1, else return the key
#     for el in arr1:
#         if el not in counter:
#             return el
#         else:
#             counter[el] -= 1

#     # All keys in the dictionary should have a value of 0
#     print(counter)

# # SOLUTION 2: Merging arrays, sorting them and looping through to get the odd counts. This solution is optimal for duplicates and cases where arr1 is shuffled from arr2 and vice versa.


# def finder2(arr1, arr2):  # O(n)
#     # Check if there are elements in the array
#     if len(arr1) < 1 or len(arr2) < 1:
#         return None

#     merged = sorted(arr1 + arr2)

#     for el in merged:
#         if merged.count(el) % 2 != 0:
#             return el
#     return None

# # SOLUTION 3: Sorting arrays, applying zip and looping through to find missing element.


# def finder3(arr1, arr2):  # O(nlogn)
#     # Check if there are elements in the array
#     if len(arr1) < 1 or len(arr2) < 1:
#         return None

#     arr1.sort()
#     arr2.sort()

#     for i, j in zip(arr1, arr2):
#         # print(zip(arr1, arr2))
#         # print(i, j)
#         if i != j:

#             return i
#     return arr1[-1]
