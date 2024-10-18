"""
Comparison Operators

When coding it's necessary to be able to compare two values. Boolean logic is the name for these kinds of comparison operations that always result in True or False.

The operators:

    < "less than"
    > "greater than"
    <= "less than or equal to"
    >= "greater than or equal to"
    == "equal to"
    != "not equal to"

For example:

5 < 6 # evaluates to True
5 > 6 # evaluates to False
5 >= 6 # evaluates to False
5 <= 6 # evaluates to True
5 == 6 # evaluates to False
5 != 6 # evaluates to True

Assignment

Complete the player_1_wins function. It should return True if player 1 has a higher score, and False otherwise.
"""

def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score


"""
---------------------------------
Inputs: 5, 6
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 5, 5
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 7, 6
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 10, 3
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 2, 2
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 0, 0
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 10, 5
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 5, 10
Expecting: False
Actual: False
Pass
============= PASS ==============
8 passed, 0 failed
"""