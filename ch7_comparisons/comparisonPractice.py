"""
Comparison Practice

car_size = 4
truck_size = 5
is_smaller = car_size < truck_size
# is_smaller is True 

Assignment

Complete the can_withstand_blow function. It should return True if the hero's armor is greater than or equal to the damage dealt by the enemy, and False otherwise.
"""

def can_withstand_blow(hero_armor, enemy_damage):
    result = hero_armor >= enemy_damage
    return result


"""
---------------------------------
Inputs: 175, 250
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 250, 175
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 250, 250
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 0, 0
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 1, 1
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 2, 3
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 3, 2
Expecting: True
Actual: True
Pass
============= PASS ==============
7 passed, 0 failed
"""