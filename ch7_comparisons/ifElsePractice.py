"""
If-Else Practice

Here are some basic rules with if/else blocks.

    You can't have an elif or an else without an if
    You can have an else without an elif

Remember, to check if two values are the same use the == operator.

same = 5 == 6
# same is False

same = 6 == 6
# same is True

Assignment

There is a bug in the check_high_score function! Add the proper conditional statement to fix the bug. If the names match, return the string:

You are the highest scoring player!

Otherwise, return:

You are not the highest scoring player!
"""

def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"


"""
---------------------------------
Inputs: ash ketchum, ash ketchum
Expecting: You are the highest scoring player!
Actual: You are the highest scoring player!
Pass
---------------------------------
Inputs: brock, ash ketchum
Expecting: You are not the highest scoring player!
Actual: You are not the highest scoring player!
Pass
---------------------------------
Inputs: misty, brock
Expecting: You are not the highest scoring player!
Actual: You are not the highest scoring player!
Pass
---------------------------------
Inputs: ,
Expecting: You are the highest scoring player!
Actual: You are the highest scoring player!
Pass
---------------------------------
Inputs: same, same
Expecting: You are the highest scoring player!
Actual: You are the highest scoring player!
Pass
============= PASS ==============
5 passed, 0 failed
"""