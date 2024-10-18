"""
Minimum number in Python
Assignment

Write a function called find_min() that finds the smallest number in a list

find_min([1, 3, -1, 2]) -> -1

find_min([18, 3, 7, 2]) -> 2
Positive infinity

Since you're trying to keep track of the smallest number, start with a really big number. Python has a built-in constant that represents positive infinity.

min = float("inf")
"""

def find_min(nums):
    min = float('inf')
    for num in nums:
        if num < min:
            min = num
    return min


"""
---------------------------------
Inputs: [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
Expecting: -4
Actual: -4
Pass
---------------------------------
Inputs: [4, 3, 2, 1, 18, 1, 2, 3, 4, 5, 6, 7]
Expecting: 1
Actual: 1
Pass
---------------------------------
Inputs: [43, 234, 65465, 234, 2343, 443, 2123, 8768]
Expecting: 43
Actual: 43
Pass
---------------------------------
Inputs: [0]
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs: [-1, -2, -3]
Expecting: -3
Actual: -3
Pass
---------------------------------
Inputs: [100, 200, 300]
Expecting: 100
Actual: 100
Pass
============= PASS ==============
6 passed, 0 failed
"""