"""
Python Numbers

In Python, numbers without a decimal point are called Integers - just like they are in mathematics.

Integers are simply whole numbers, positive or negative. For example, 3 and -3 are both examples of integers.

Arithmetic can be performed as you might expect:
Addition

2 + 1
# 3

Subtraction

2 - 1
# 1

Multiplication

2 * 2
# 4

Division

3 / 2
# 1.5 (a float)

This one is actually a bit different - division on two integers will actually produce a float. A float is, as you may have guessed, the number type that allows for decimal values.

Assignment

Complete the missing sections of the calculate_damage function.

    Fix the total_damage variable so that it contains the sum of all the different weapons' damage values.
    Fix the average_damage variable so that it contains the average weapon damage.

"""

def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = (sword + arrow + spear + dagger + fireball) / 5
    return total_damage, average_damage


"""
---------------------------------
Inputs: 3, 5, 2, 1, 4
Expecting: (15, 3.0)
Actual: (15, 3.0)
Pass
---------------------------------
Inputs: 5, 5, 5, 5, 5
Expecting: (25, 5.0)
Actual: (25, 5.0)
Pass
---------------------------------
Inputs: 1, 2, 3, 4, 5
Expecting: (15, 3.0)
Actual: (15, 3.0)
Pass
---------------------------------
Inputs: 0, 0, 0, 0, 10
Expecting: (10, 2.0)
Actual: (10, 2.0)
Pass
---------------------------------
Inputs: 0, 0, 0, 0, 0
Expecting: (0, 0.0)
Actual: (0, 0.0)
Pass
---------------------------------
Inputs: 10, 20, 30, 40, 50
Expecting: (150, 30.0)
Actual: (150, 30.0)
Pass
---------------------------------
Inputs: 2, 2, 2, 2, 2
Expecting: (10, 2.0)
Actual: (10, 2.0)
Pass
---------------------------------
Inputs: 1, 1, 1, 1, 1
Expecting: (5, 1.0)
Actual: (5, 1.0)
Pass
============= PASS ==============
8 passed, 0 failed
"""