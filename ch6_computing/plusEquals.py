"""
Plus Equals

Python makes reassignment easy when doing math. In JavaScript or Go, you might be familiar with the ++ syntax for incrementing a number variable by 1. In Python, we use the += in-place operator instead.

star_rating = 4
star_rating += 1
# star_rating is now 5

Other operators

The other in-place operators work similarly:

star_rating = 4
star_rating -= 1
# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2
# star_rating is now 2.0

Assignment

Complete the get_hurt function. It should use the -= in-place operator to subtract damage from current_health and then return the new current_health.
Tip

You cannot use -= in a return statement. Set the variable first, and then return it after!

"""

def get_hurt(current_health, damage):
    current_health -= damage
    return current_health


"""
---------------------------------
Inputs: 1000, 100
Expecting: 900
Actual: 900
Pass
---------------------------------
Inputs: 900, 60
Expecting: 840
Actual: 840
Pass
---------------------------------
Inputs: 840, 10
Expecting: 830
Actual: 830
Pass
---------------------------------
Inputs: 830, 3
Expecting: 827
Actual: 827
Pass
---------------------------------
Inputs: 0, 0
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs: 1, 1
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs: 100, 2
Expecting: 98
Actual: 98
Pass
---------------------------------
Inputs: 2500, 3
Expecting: 2497
Actual: 2497
Pass
============= PASS ==============
8 passed, 0 failed
"""