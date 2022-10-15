"""
TWO SUMS
https://leetcode.com/problems/two-sum/ 1
Given an array of integers nums and an integer target, return the two numbers such that they add up to target.
"""
#SOLUTION 1: Using brute force
#O(N^2) TIME AND O(1) SPACE
def twoSum1(nums, target):
    for i in range(len(nums)-1):
        firstnum = nums[i]
        for j in range(i+1, len(nums)):
            secondnum = nums[j]
            if firstnum + secondnum == target:
                return [firstnum, secondnum]
    return []

#SOLUTION 2: Using pointers
#O(N LOGN) TIME COS OF Python Sort() AND O(1) SPACE
def twoSum2(nums, target):
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
def twoSum3(nums, target):
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
def twoSum4(nums, target):
    sums = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in sums:
            return [sums[diff], idx]
        sums[num] = idx
    return []