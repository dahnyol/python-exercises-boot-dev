"""
Random Events

The Fantasy Quest team has been working on a new feature: random events! These new events are ready to go but they need a way to trigger in the open world for players to experience them.
Assignment

The team wants the random events to trigger on prime numbers. Write a function that takes a single number as input and returns True if it is a prime number or False if it is not.
What is a prime number?

A prime number is a positive integer, greater than 1, that is only divisible by itself and 1. For example, 2, 3, 5, and 7 are all prime numbers, but 1, 4, 6, 8, and 9 are not.
Tip

0 and 1 are not prime numbers! And don't forget to catch all negative numbers!

We'll talk more about it next chapter, but you can use the modulo operator % to find a remainder. For example, 7 modulo 2 would be 1, because 2 can be multiplied evenly into 7 at most 3 times.

remainder = 8 % 3
# remainder = 2

remainder = 9 % 3
# remainder = 0

If you get stuck, feel free to move ahead and come back after learning more about the modulo operator.
"""
# Returning False for numbers less than or equal to 1.

# Iterating through potential factors from 2 up to the square root of the number.

# If a factor is found that divides the number evenly, it returns False.

# If no factors are found, it returns True.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return 

"""
---------------------------------
Input number: 7
Expecting: True
Actual: None
Fail
---------------------------------
Input number: -7
Expecting: False
Actual: False
Pass
---------------------------------
Input number: 9
Expecting: False
Actual: False
Pass
---------------------------------
Input number: 23
Expecting: True
Actual: None
Fail
---------------------------------
Input number: -1
Expecting: False
Actual: False
Pass
---------------------------------
Input number: 0
Expecting: False
Actual: False
Pass
---------------------------------
Input number: 1
Expecting: False
Actual: False
Pass
---------------------------------
Input number: 2
Expecting: True
Actual: None
Fail
---------------------------------
Input number: 4
Expecting: False
Actual: False
Pass
---------------------------------
Input number: 31
Expecting: True
Actual: None
Fail
---------------------------------
Input number: 100
Expecting: False
Actual: False
Pass
============= FAIL ==============
7 passed, 4 failed
"""