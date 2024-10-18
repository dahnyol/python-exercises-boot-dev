"""
Appending in Python

It's common to create an empty list then fill it with values using a loop. We can add values to the end of a list using the .append() method:

cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']

Assignment

We need to generate a unique user ID for each player in the game. An ID is just a unique number that identifies a user.

Let's finish the generate_user_list function. In the body of the loop, use the incrementing value i as unique IDs and append them to the player_ids list.
"""

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids


"""
---------------------------------
Inputs: 5
Expecting: [0, 1, 2, 3, 4]
Actual: [0, 1, 2, 3, 4]
Pass
---------------------------------
Inputs: 10
Expecting: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Actual: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Pass
---------------------------------
Inputs: 0
Expecting: []
Actual: []
Pass
---------------------------------
Inputs: 1
Expecting: [0]
Actual: [0]
Pass
---------------------------------
Inputs: 100
Expecting: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 
54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
Actual: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 
82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
Pass
---------------------------------
Inputs: 25
Expecting: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]        
Actual: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
Pass
---------------------------------
Inputs: 50
Expecting: [0, 1, 2, 3
"""