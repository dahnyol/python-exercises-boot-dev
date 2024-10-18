"""
Even teams

Fantasy Quest is having a problem where Battleground teams are uneven when the match begins. We need a function that will correctly split the two teams evenly.
Assignment

Complete the split_players_into_teams function. Use a slice with a "step" to create two new lists from the players list:

    even_team should have the players with even-numbered indexes.
    odd_team should have the players with odd-numbered indexes.

Return even_team and odd_team in that order. Be careful not to assign the wrong values to these variables!
Hint

You might want to use a slice with a "step" value:

my_list[ start : stop : step ]
"""

def split_players_into_teams(players):
    even_team = players[::2]
    odd_team = players[1::2] 
    
    return even_team, odd_team


"""
---------------------------------
Inputs: ['Harry', 'Hermione', 'Ron', 'Ginny', 'Fred', 'Neville', 'Draco', 'Luna', 'Cho', 'Gregory', 'Lee', 'Michael', 'Lavender', 'Frank', 'Anthony', 'Allan']
Expecting: (['Harry', 'Ron', 'Fred', 'Draco', 'Cho', 'Lee', 'Lavender', 'Anthony'], ['Hermione', 'Ginny', 'Neville', 'Luna', 'Gregory', 'Michael', 'Frank', 'Allan'])
Actual: (['Harry', 'Ron', 'Fred', 'Draco', 'Cho', 'Lee', 'Lavender', 'Anthony'], ['Hermione', 'Ginny', 'Neville', 'Luna', 'Gregory', 'Michael', 'Frank', 'Allan'])
Pass
---------------------------------
Inputs: ['Mike', 'Walter', 'Skyler', 'Tuco']
Expecting: (['Mike', 'Skyler'], ['Walter', 'Tuco'])
Actual: (['Mike', 'Skyler'], ['Walter', 'Tuco'])
Pass
---------------------------------
Inputs: ['Alice', 'Bob', 'Charlie', 'David']
Expecting: (['Alice', 'Charlie'], ['Bob', 'David'])
Actual: (['Alice', 'Charlie'], ['Bob', 'David'])
Pass
---------------------------------
Inputs: []
Expecting: ([], [])
Actual: ([], [])
Pass
============= PASS ==============
4 passed, 0 failed
"""