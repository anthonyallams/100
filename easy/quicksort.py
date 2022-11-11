"""
QUICK SORT
Given an list of values, perform QUICK sort and evaluate it
"""
#SOLUTION 1: Using iterative approach
#O(NLOG N) TIME AND O(N) SPACE
from random import randint
def quick_sort1(nums):
    if len(nums) < 2:
        return nums
    
    pivot = nums[randint(0, len(nums)-1)]
    low, same, high = [],[],[]

    for num in nums:
        if num > pivot:
            high.append(num)
        elif num == pivot:
            same.append(num)
        else:
            low.append(num)
            
    return quick_sort1(low) + same + quick_sort1(high)
