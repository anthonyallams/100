"""
BUBBLE SORT
Given an list of values, perform Bubble sort and evaluate it
"""


# Using iterative approach with double loop and counter for optimization
# O(N) TIME AND O(N) SPACE
def bubble_sort1(nums):
    for i in range(len(nums) - 1, 0, -1):
        already_sorted = True
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                already_sorted = False
        if already_sorted:
            break
    return nums
