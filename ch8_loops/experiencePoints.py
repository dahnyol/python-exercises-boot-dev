"""
Experience Points

You've been hired by a game studio to work on their latest role-playing game. In this game adventurers need experience points (XP) to level up and become stronger. You've been tasked with creating a function to calculate the total amount of XP needed for a player to reach a specific level.

Each character starts with 0 XP at level 1. To reach the next level, they need XP equal to their current level times 5.
Level 	Total XP Gained 	XP To Next Level
1 	0 	5
2 	5 	10
3 	15 	15
4 	30 	20
Assignment

Complete the calculate_experience_points function.

The calculate_experience_points function takes a single parameter named level. Determine the total XP needed to reach the specified level from level 1 and return it.
"""

def calculate_experience_points(level):
    xp_to_next_level = 0 
    for i in range(1, level):
        xp_to_next_level += 5 * i
    return xp_to_next_level

"""
---------------------------------
Inputs: 2
Expecting: 5
Actual: 5
Pass
---------------------------------
Inputs: 3
Expecting: 15
Actual: 15
Pass
---------------------------------
Inputs: 4
Expecting: 30
Actual: 30
Pass
---------------------------------
Inputs: 1
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs: 5
Expecting: 50
Actual: 50
Pass
---------------------------------
Inputs: 7
Expecting: 105
Actual: 105
Pass
---------------------------------
Inputs: 10
Expecting: 225
Actual: 225
Pass
---------------------------------
Inputs: 15
Expecting: 525
Actual: 525
Pass
---------------------------------
Inputs: 20
Expecting: 950
Actual: 950
Pass
============= PASS ==============
9 passed, 0 failed
"""