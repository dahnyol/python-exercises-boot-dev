"""
If-Else Practice

Here are some basic rules with if/else blocks.

    You can't have an elif or an else without an if
    You can have an else without an elif

Assignment

Complete the check_high_score function. If the player_name matches the high score name, return the string:

high

Otherwise, if it's the low scorer, return the string:

low

Otherwise, return the string:

neither
"""

def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return 'high'
    if player_name == low_scoring_player_name:
        return 'low'
    return 'neither'


"""
---------------------------------
Player Name: ash ketchum, High Scoring Player: ash ketchum, Low Scoring Player: brock
Expecting: high
Actual: high
Pass
---------------------------------
Player Name: brock, High Scoring Player: ash ketchum, Low Scoring Player: brock
Expecting: low
Actual: low
Pass
---------------------------------
Player Name: misty, High Scoring Player: brock, Low Scoring Player: ash ketchum
Expecting: neither
Actual: neither
Pass
---------------------------------
Player Name: red, High Scoring Player: red, Low Scoring Player: blue
Expecting: high
Actual: high
Pass
---------------------------------
Player Name: blue, High Scoring Player: red, Low Scoring Player: blue
Expecting: low
Actual: low
Pass
---------------------------------
Player Name: green, High Scoring Player: red, Low Scoring Player: blue
Expecting: neither
Actual: neither
Pass
============= PASS ==============
6 passed, 0 failed
"""