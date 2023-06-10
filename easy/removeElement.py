"""
REMOVE ELEMENT
https://leetcode.com/problems/remove-element/
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements 
may be changed.Since it is impossible to change the length of the array in some languages, you must instead have the result be  
placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements 
of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


# SOLUTION 1: Using a count to get the number of val elements in the nums list
# O(N) TIME AND O(1) SPACE
def removeElement(nums: list, val: int) -> int:
    """
    Initialize counter k
    Loop through len of nums and if element is not val, increment counter and change element
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


# SOLUTION 2: Enhanced moveZeros/Using a pointer to move val to last position in loop and count occurence
# O(N) TIME AND O(1) SPACE
def removeElement1(nums: list, val: int) -> int:
    """
    Initialize left pointer/counter
    Loop through the len of nums using right pointer and check if element is val
    If not val, change position of  vals to the end and incrementing the left (count/point)er
    """
    l = 0
    for r in range(len(nums)):
        # breakpoint()
        if nums[r] != val:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return l


# SOLUTION 3: Using inbuilt methods -O(N) TIME AND O(1) SPACE
def removeElement2(nums: list, val: int) -> int:
    return len([x for x in nums if x != val])
