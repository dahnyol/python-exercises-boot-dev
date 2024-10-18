"""
Challenges

In this chapter we are going to practice applying the skills and concepts we learned while building "Fantasy Quest"
Number Sum

Write a function called number_sum(n) that adds up all the numbers from 1 to n. For example:

number_sum(5) -> 1+2+3+4+5 -> 15

number_sum(3) -> 1+2+3 -> 6
"""

def number_sum(n):
    sum = 0
    
    for i in range(1, n + 1): # n + 1 because range end is exclusive
        sum += i
    return sum


# gauss summation
def number_sum(n):
    sum =  n * (n + 1) / 2
    return sum
"""
---------------------------------
Inputs: 3
Expecting: 6
Actual: 6
Pass
---------------------------------
Inputs: 5
Expecting: 15
Actual: 15
Pass
---------------------------------
Inputs: 1
Expecting: 1
Actual: 1
Pass
---------------------------------
Inputs: 18
Expecting: 171
Actual: 171
Pass
---------------------------------
Inputs: 0
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs: 227
Expecting: 25878
Actual: 25878
Pass
---------------------------------
Inputs: 100
Expecting: 5050
Actual: 5050
Pass
---------------------------------
Inputs: 500
Expecting: 125250
Actual: 125250
Pass
============= PASS ==============
8 passed, 0 failed
"""