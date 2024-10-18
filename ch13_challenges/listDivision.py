"""
List Division

Write a function called divide_list() that takes a list and a number as input. The function returns a new list that contains all the elements of the original list except they have been divided by the second input.

divided_list = divide_list([6, 8, 10], 2)
print(divided_list) # [3.0, 4.0, 5.0]

Make sure you're appending the raw float values. Don't round or cast the numbers to integers.
"""

def divide_list(nums, divisor):
    divided_list = []

    for num in nums:
        divided = num / divisor
        divided_list.append(divided)
    
    return divided_list


"""
---------------------------------
Inputs:
 * List of numbers: [6, 8, 10]
 * Divisor: 2
Expecting: [3.0, 4.0, 5.0]
Actual: [3.0, 4.0, 5.0]
Pass
---------------------------------
Inputs:
 * List of numbers: [1, 2, 3, 4]
 * Divisor: 1
Expecting: [1.0, 2.0, 3.0, 4.0]
Actual: [1.0, 2.0, 3.0, 4.0]
Pass
---------------------------------
Inputs:
 * List of numbers: [15, 30, 45]
 * Divisor: 3
Expecting: [5.0, 10.0, 15.0]
Actual: [5.0, 10.0, 15.0]
Pass
---------------------------------
Inputs:
 * List of numbers: [0]
 * Divisor: 1
Expecting: [0.0]
Actual: [0.0]
Pass
---------------------------------
Inputs:
 * List of numbers: [27, 54, 81]
 * Divisor: 9
Expecting: [3.0, 6.0, 9.0]
Actual: [3.0, 6.0, 9.0]
Pass
---------------------------------
Inputs:
 * List of numbers: [100, 200, 300, 400]
 * Divisor: 10
Expecting: [10.0, 20.0, 30.0, 40.0]
Actual: [10.0, 20.0, 30.0, 40.0]
Pass
============= PASS ==============
6 passed, 0 failed
"""