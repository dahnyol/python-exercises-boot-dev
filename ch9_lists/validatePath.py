"""
Validate Path

The Fantasy Quest is implementing a new type of quest that requires a player to follow a specific path in order to complete the quest.
Assignment

Complete the validate_path function. It should compare the expected sequence of waypoints with the actual sequence taken by a character and calculate how accurately the character followed the intended path.
Inputs

    expected_path: A list of waypoints that define the correct path for the quest.
    character_path: A list where the first index is the name of the character, and the rest of the list consists of the waypoints they actually visited.

Output

The function should return 2 values:

    character_name: a string
    percentage: a float

Example

expected_path = ["A", "B", "C", "D"]
character_path = ["Hero123", "A", "X", "C", "D"]
name, percent = validate_path(expected_path, character_path)
print(name, percent)
# prints: Hero123, 75.0
"""

def validate_path(expected_path, character_path):
    char_name = character_path[0]
    char_path = character_path[1:]
    counter = 0
    
    for i in range(0, len(expected_path)):
        if expected_path[i] == char_path[i]:
            counter += 1
    
    complete_percent = (counter / len(expected_path)) * 100
    return char_name, complete_percent


"""
---------------------------------
Inputs:
expected_path: ['A', 'B', 'C', 'D', 'E']
character_path: ['Dellbi', 'A', 'B', 'C', 'D', 'E']
Expecting: ('Dellbi', 100.0)
Actual: ('Dellbi', 100.0)
Pass
---------------------------------
Inputs:
expected_path: ['A', 'B', 'C', 'D', 'E']
character_path: ['Kaladin', 'A', 'X', 'C', 'D', 'E']
Expecting: ('Kaladin', 80.0)
Actual: ('Kaladin', 80.0)
Pass
---------------------------------
Inputs:
expected_path: ['A', 'B', 'C', 'D', 'E']
character_path: ['ShadowWalker', 'X', 'X', 'X', 'X', 'X']
Expecting: ('ShadowWalker', 0.0)
Actual: ('ShadowWalker', 0.0)
Pass
---------------------------------
Inputs:
expected_path: ['A', 'B', 'C', 'D', 'E']
character_path: ['Jamie', 'A', 'B', 'X', 'X', 'E']
Expecting: ('Jamie', 60.0)
Actual: ('Jamie', 60.0)
Pass
---------------------------------
Inputs:
expected_path: ['A', 'B', 'C', 'D', 'E']
character_path: ['Odium', 'A', 'B', 'C', 'D', 'E']
Expecting: ('Odium', 100.0)
Actual: ('Odium', 100.0)
Pass
============= PASS ==============
5 passed, 0 failed
"""