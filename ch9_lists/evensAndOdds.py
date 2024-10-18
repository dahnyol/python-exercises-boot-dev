"""
Evens and odds

You've been asked to write a program that will calculate how many odd and even numbers exist in a list.
Challenge

Write the get_odds_and_evens function to loop through the numbers list and check if each number in the list is either odd or even.

Increment the num_evens counter if even, and the num_odds counter if it's odd. Lastly, return the two values num_odds and num_evens in that order.
Tip

Remember, you can check if a number is divisible by another number using the modulo operator (%) and comparing the result.

def divisible_by_5(num):
    return num % 5 == 0


print(divisible_by_5(20))
# True
print(divisible_by_5(19))
# False
"""

def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0

    # Don't touch above this line
    for num in numbers:
        if num % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    return num_odds, num_evens
    

"""
---------------------------------
Inputs: [1, 7, 2, 5, 3, 4]
Expecting: (4, 2)
Actual: (4, 2)
Pass
---------------------------------
Inputs: [0, 99, 2, 33, 61, 44, 9, 10, 12, 240, 35, 9082, 1234]
Expecting: (5, 8)
Actual: (5, 8)
Pass
---------------------------------
Inputs: []
Expecting: (0, 0)
Actual: (0, 0)
Pass
---------------------------------
Inputs: [1, 3, 5, 7, 9]
Expecting: (5, 0)
Actual: (5, 0)
Pass
---------------------------------
Inputs: [2, 4, 6, 8, 10]
Expecting: (0, 5)
Actual: (0, 5)
Pass
---------------------------------
Inputs: [1]
Expecting: (1, 0)
Actual: (1, 0)
Pass
---------------------------------
Inputs: [2]
Expecting: (0, 1)
Actual: (0, 1)
Pass
---------------------------------
Inputs: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expecting: (5, 5)
Actual: (5, 5)
Pass
============= PASS ==============
8 passed, 0 failed
"""