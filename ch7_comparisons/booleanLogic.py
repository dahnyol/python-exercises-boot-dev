"""
Boolean Logic

Boolean logic refers to logic dealing with boolean (True or False) values. For example,

Dogs must have four legs and weigh less than 100 kilograms. (Both conditions must be true)

Cars are cool if they go faster than 200 MPH, or if they are electric. (At least one condition must be true)
Logical operators review

As we discussed earlier, the logical operators and and or can be used to perform boolean logic.
And review

The and operator returns True if both of the conditions on either side evaluates to True:

def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100

Let's go over how this function evaluates the parameters num_legs=4 and weight=99:

return 4 == 4 and 99 < 100

return True and True

return True

Let's see what would happen with 3 and 98 instead:

return 3 == 4 and 98 < 100

return False and True

return False

Or review

The or operator returns True if at least one of the conditions on either side evaluates to True:

def is_car_cool(speed, is_electric):
    return speed > 200 or is_electric

Let's use a non-electric car that can do 250:

return 250 > 200 or False

return True or False

return True

Assignment

We need a way for our game to track whether a character's attack hits or misses.

Complete the does_attack_hit function. The function should return True if either of the following conditions are met:

    The attack_roll is not a 1 and the attack roll is greater than or equal to the armor_class, or
    The attack roll is a 20

Otherwise, it should return False.
Tip

Remember that you can define the order of operations using parentheses:

# The college admits students with a high GPA and high SAT score
# or anyone who is just rich
should_admit = (high_gpa and high_sat_score) or (is_rich)
"""

def does_attack_hit(attack_roll, armor_class):
    if attack_roll == 20 or attack_roll != 1 and attack_roll >= armor_class:
        return True
    return False


"""
---------------------------------
Inputs: 17, 18
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 20, 25
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 1, 0
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 16, 13
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 5, 5
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 1, 1
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 20, 20
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 15, 10
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 2, 3
Expecting: False
Actual: False
Pass
============= PASS ==============
9 passed, 0 failed
"""