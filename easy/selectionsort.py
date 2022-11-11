"""
SELECTION SORT
Given an list of values, perform selection sort and evaluate it
"""
#SOLUTION 1: Using a double loop
#O(N^2) TIME AND O(1) SPACE
def selection_sort1(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j], nums[i]
    return nums