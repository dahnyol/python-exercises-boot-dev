"""
Combat Advantage

Fantasy Quest doesn't have any way for players to know if they are strong enough to fight certain enemies.

    If a player's power level is greater than the enemy's defense that player has an advantage
    If the player's power and enemy's defense are equal, they are evenly matched
    Otherwise, that player has a disadvantage.

Assignment

On line 4 write an if/elif/else block. Using the rules specified above, set advantage, disadvantage, or evenly_matched to True depending on the values of player_power and enemy_defense.

For example, if the player's power is greater than the enemy's defense, advantage should be set to True. etc.
"""

def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage = True
    elif player_power == enemy_defense:
        evenly_matched = True
    else:
        disadvantage = True

    return advantage, disadvantage, evenly_matched


"""
---------------------------------
Inputs: 101, 100
Expecting: True, False, False    
Actual: (True, False, False)     
Pass
---------------------------------
Inputs: 50, 100
Expecting: False, True, False    
Actual: (False, True, False)     
Pass
---------------------------------
Inputs: 100, 100
Expecting: False, False, True    
Actual: (False, False, True)     
Pass
---------------------------------
Inputs: 150, 70
Expecting: True, False, False    
Actual: (True, False, False)     
Pass
---------------------------------
Inputs: 80, 150
Expecting: False, True, False    
Actual: (False, True, False)
Pass
---------------------------------
Inputs: 0, 0
Expecting: False, False, True
Actual: (False, False, True)
Pass
---------------------------------
Inputs: 1, 1
Expecting: False, False, True
Actual: (False, False, True)
Pass
---------------------------------
Inputs: 1000, 500
Expecting: True, False, False
Actual: (True, False, False)
Pass
---------------------------------
Inputs: 500, 1000
Expecting: False, True, False
Actual: (False, True, False)
Pass
============= PASS ==============
9 passed, 0 failed
"""