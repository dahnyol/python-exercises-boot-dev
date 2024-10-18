"""
Sum Game

Remember you can use in-place operators to increase or decrease a variable by any amount.

number_of_enemies = 10
number_of_enemies += 2
# number_of_enemies is 12

number_of_enemies = 10
number_of_enemies -= 2
# number_of_enemies is 8

Assignment

Fix the bug in the sum_of_numbers function. Instead of adding 1 to total at each iteration of the loop, it should add i. For example, instead of:

1 + 1 + 1 + 1 + 1...

we want:

0 + 1 + 2 + 3 + 4...

The desired output is a single number after the loop has finished executing.
"""

def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total


"""
---------------------------------
Inputs:
 * start: 0
 * end: 5
Expecting: 10
Actual: 10
Pass
---------------------------------
Inputs:
 * start: 0
 * end: 10
Expecting: 45
Actual: 45
Pass
---------------------------------
Inputs:
 * start: 10
 * end: 20
Expecting: 145
Actual: 145
Pass
---------------------------------
Inputs:
 * start: 1
 * end: 100
Expecting: 4950
Actual: 4950
Pass
---------------------------------
Inputs:
 * start: 5
 * end: 50
Expecting: 1215
Actual: 1215
Pass
---------------------------------
Inputs:
 * start: 20
 * end: 30
Expecting: 245
Actual: 245
Pass
---------------------------------
Inputs:
 * start: 50
 * end: 60
Expecting: 545
Actual: 545
Pass
---------------------------------
Inputs:
 * start: 100
 * end: 110
Expecting: 1045
Actual: 1045
Pass
============= PASS ==============
8 passed, 0 failed
"""