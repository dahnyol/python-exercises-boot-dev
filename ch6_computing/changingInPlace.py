"""
Changing In Place

It's fairly common to want to change the value of a variable based on its current value.

player_score = 4
player_score = player_score + 1
# player_score now equals 5

player_score = 4
player_score = player_score - 1
# player_score now equals 3

Don't let the fact that the expression player_score = player_score - 1 is not a valid mathematical expression be confusing. It doesn't matter, it is valid code. It's valid because the way the expression should be read in English is:

    Assign to player_score the current value of player_score minus 1

In this operation, the right-hand side (player_score - 1) is calculated first. Once we have the result, we update player_score with this new value.
Assignment

Complete the update_player_score function. It should add increment to current_score and then return the new current_score.
"""

def update_player_score(current_score, increment):
    current_score = current_score + increment
    return current_score


"""
---------------------------------
Inputs: 0, 100
Expecting: 100
Actual: 100
Pass
---------------------------------
Inputs: 100, 200
Expecting: 300
Actual: 300
Pass
---------------------------------
Inputs: 300, 300
Expecting: 600
Actual: 600
Pass
---------------------------------
Inputs: 600, 50
Expecting: 650
Actual: 650
Pass
---------------------------------
Inputs: 0, 0
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs: 1, 1
Expecting: 2
Actual: 2
Pass
---------------------------------
Inputs: 100, -50
Expecting: 50
Actual: 50
Pass
============= PASS ==============
7 passed, 0 failed
"""