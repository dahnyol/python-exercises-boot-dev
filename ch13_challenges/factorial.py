"""
Factorial

Complete the factorial() function. It should calculate the factorial of a number. A factorial of a number is the product of all positive integers less than or equal to that number.

For example:

4! = 4 * 3 * 2 * 1 = 24

Note: In mathematics, the ! symbol denotes a factorial, but is not used in Python.
Tip: A special case for zero

The value of 0! is 1. This keeps factorials consistent with the convention for an empty product.
"""

def factorial(num):
    total = 1
    
    for i in range(1, num + 1):
        total *= i
    return total


"""
---------------------------------
Inputs: 0
Expecting: 1
Actual: 1
Pass
---------------------------------
Inputs: 4
Expecting: 24
Actual: 24
Pass
---------------------------------
Inputs: 1
Expecting: 1
Actual: 1
Pass
---------------------------------
Inputs: 5
Expecting: 120
Actual: 120
Pass
---------------------------------
Inputs: 7
Expecting: 5040
Actual: 5040
Pass
---------------------------------
Inputs: 9
Expecting: 362880
Actual: 362880
Pass
---------------------------------
Inputs: 13
Expecting: 6227020800
Actual: 6227020800
Pass
---------------------------------
Inputs: 15
Expecting: 1307674368000
Actual: 1307674368000
Pass
============= PASS ==============
8 passed, 0 failed
"""