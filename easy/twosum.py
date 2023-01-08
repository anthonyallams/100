"""
TWO SUMS
https://leetcode.com/problems/two-sum/ 1
Given an array of integers nums and an integer target, return the two numbers such that they add up to target.
"""
#SOLUTION 1: Using brute force
#O(N^2) TIME AND O(1) SPACE
def twoSum1(nums:list[int], target:int)->list[int]:
    """
    Loop through the list with index i and initialize the first number 
    Loop through subsequent elements with index j and initialize second number
    If addition of first num and second num equals the target, return it else [].  
    """
    for i in range(len(nums)-1):
        firstnum = nums[i]
        for j in range(i+1, len(nums)):
            secondnum = nums[j]
            if firstnum + secondnum == target:
                return [firstnum, secondnum]
    return []

#SOLUTION 2: Using pointers
#O(N LOGN) TIME COS OF Python Sort() AND O(1) SPACE
def twoSum2(nums:list[int], target:int)->list[int]:
    """
    Initialize left and right pointers
    Loop through the array with curent sum as addition of nums[left] + nums[right]
    if current sum equals target, return left and right nums else increment or decrement pointers
    """
    nums.sort()
    left, right = 0, len(nums)-1
    while left <= right:
        leftNum, rightNum = nums[left], nums[right]
        curSum = leftNum + rightNum
        if curSum == target:
            return [leftNum, rightNum]
        elif curSum > target:
            right -= 1
        else:
            left += 1
    return []

#SOLUTION 3: Using hashmap
#O(N) TIME AND O(N) SPACE
def twoSum3(nums:list[int], target:int)->list[int]:
    '''
    Initialize the sums hashmap
    Loop through the array and set target as sum of difference and num
    Add difference to hashmap if not else return difference and num
    '''
    sums = {}
    for num in nums:
        diff = target - num
        if diff in sums:
            return [diff, num]
        sums[num] = diff
    return []



"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""
#Using hashmap
#O(N) TIME AND O(N) SPACE 
def twoSum4(nums, target):
    sums = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in sums:
            return [sums[diff], idx]
        sums[num] = idx
    return []