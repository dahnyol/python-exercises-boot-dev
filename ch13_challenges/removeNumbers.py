"""
Remove Numbers

Complete the remove_nonints() function that takes a list and returns a new list with all the non-integer types removed.

remove_nonints(['1', 1, '3', '400', 4, 500])
# Remaining list after removing nonints = [1, 4, 500]

You can check the type of a variable using type() function.

if type(variable) == int:

Do not change the input nums list, return a new list with only the integers.
"""

def remove_nonints(nums):
    only_ints = []
    for num in nums:
        if type(num) == int:
            only_ints.append(num)
    return only_ints


"""
---------------------------------
Inputs:
 * nums: ['200', 300, 2, False, 'otherstring', 6]
Expecting: [300, 2, 6]
Actual: [300, 2, 6]
Pass
---------------------------------
Inputs:
 * nums: [True, 300, 2, False, 'otherstring', 76, 86, 'morestrings']
Expecting: [300, 2, 76, 86]
Actual: [300, 2, 76, 86]
Pass
---------------------------------
Inputs:
 * nums: [300, 300, 2, False, 'otherstring', 6, {}, 16]
Expecting: [300, 300, 2, 6, 16]
Actual: [300, 300, 2, 6, 16]
Pass
---------------------------------
Inputs:
 * nums: ['200', 300, 2, False, 'something', 7, 'something else']
Expecting: [300, 2, 7]
Actual: [300, 2, 7]
Pass
---------------------------------
Inputs:
 * nums: ['string', True, {}, []]
Expecting: []
Actual: []
Pass
---------------------------------
Inputs:
 * nums: []
Expecting: []
Actual: []
Pass
---------------------------------
Inputs:
 * nums: [123, 456, 789]
Expecting: [123, 456, 789]
Actual: [123, 456, 789]
Pass
---------------------------------
Inputs:
 * nums: ['123', '456', '789']
Expecting: []
Actual: []
Pass
============= PASS ==============
8 passed, 0 failed
"""