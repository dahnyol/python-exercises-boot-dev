"""
Sum Game 2
Assignment

Complete the sum_of_odd_numbers function. It should calculate the sum of all the odd numbers starting at 1 up to (but not including) the given end number and return the result.
Tips

    What number should you start with if you only want odd numbers?
    How much should you increment by in each iteration of the loop to get the next odd number?
"""

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total


"""
---------------------------------
Inputs:
 * end: 4
Expecting: 4
Actual: 4
Pass
---------------------------------
Inputs:
 * end: 6
Expecting: 9
Actual: 9
Pass
---------------------------------
Inputs:
 * end: 0
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs:
 * end: 1
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs:
 * end: 2
Expecting: 1
Actual: 1
Pass
---------------------------------
Inputs:
 * end: 4
Expecting: 4
Actual: 4
Pass
---------------------------------
Inputs:
 * end: 10
Expecting: 25
Actual: 25
Pass
---------------------------------
Inputs:
 * end: 15
Expecting: 49
Actual: 49
Pass
============= PASS ==============
8 passed, 0 failed
"""