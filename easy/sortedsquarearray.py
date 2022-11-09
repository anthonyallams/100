"""
SORTED SQUARE ARRAY
Given a sorted array, square it and return new array sorted
"""
#SOLUTION ONE: Using inbuilt python sort function
#O(NLOGN) TIME AND O(N) SPACE (Worse than o(n) time)
def sortedArray1(arr):
    squared_arr = [a**2 for a in arr]
    return sorted(squared_arr)

#SOLUTION 2: Using pointers
#O(N) TIME AND O(N) SPACE
def sortedArray2(arr):
    l, r = 0, len(arr)-1
    sorted_arr = [0 for _ in arr]
    for i in reversed(range(len(arr))):
        first, last = arr[l], arr[r]
        if abs(first) > abs(last):
            sorted_arr[i] = first ** 2
            l += 1
        else:
            sorted_arr[i] = last ** 2
            r -= 1
    return sorted_arr
