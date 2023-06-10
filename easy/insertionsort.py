"""
INSERTION SORT
Given an list of values, perform INSERTION sort and evaluate it
NOTE:
Insertion sort takes an unsorted list and divides it into sorted and unsorted sublist, with sorted sublist having length of 1 and other items going to the unsorted. Items in unsorted are sublist are increasingly moved to the sorted sublist and compared, and changed positions.

"""


# SOLUTION 1: Using iterative approach
# O(N^2) TIME AND O(1) SPACE
def insertion_sort1(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums
