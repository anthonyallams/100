"""
Maximum no of ballons
https://leetcode.com/problems/maximum-number-of-balloons/
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
"""
#SOLUTION 1: Use hashmap to get num of elements in array and divide elements in strng by element of balloon
#O(N) TIME AND O(1) SPACE
def maxNumberOfBalloons(strng:str)->int:
  """
  ALGORITHM: Pass the balloon and strng strings to a counter function to get count of elements
  Loop through the elements in balloon and for each element, divide the count of element in strng by count of element in balloon
  Get the minimum and across all elements in strng and return it
  """
  countStrng = counter(strng)
  balloon = counter('balloon')

  result = len(strng)
  for a in balloon:
    result = min(result, countStrng.get(a, 0) // balloon[a])
  return result

def counter(text):
  hashmap = {}
  for t in text:
    hashmap[t] = 1 + hashmap.get(t, 0)
  return hashmap