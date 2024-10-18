"""
Raising your own exceptions

Errors are not something to be scared of. Every program that runs in production is expected to manage errors on a constant basis. Our job as developers is to handle the errors gracefully and in a way that aligns with our user's expectations.
Errors are NOT bugs

When something in our own code happens that isn't the "happy path", we should raise our own exceptions. For example, if someone passes some bad inputs to a function we write, we should not be afraid to raise an exception to let them know they did something wrong.

An error or exception is raised when something bad happens, but as long as our code handles it as users expect it to, it's not a bug. A bug is when code behaves in ways our users don't expect it to.

For example, if a player tries to forge a sword out of a metal bar, we might raise an exception if the game doesn't support crafting a sword from that metal type.

def craft_sword(metal_bar):
    if metal_bar == "bronze":
        return "bronze sword"
    if metal_bar == "iron":
        return "iron sword"
    if metal_bar == "steel":
        return "steel sword"
    raise Exception("invalid metal bar")

However, that's the expected behavior of the game, so it's not a bug. If a player can forge a sword out of gold, that may be considered a bug because that's against the rules of the game.
Don't catch your own exceptions

As a rule of thumb, you do not want to catch exceptions you raise within the same function block, for example:

def craft_sword(metal_bar):
    try:
        if metal_bar == "bronze":
            return "bronze sword"
        if metal_bar == "iron":
            return "iron sword"
        if metal_bar == "steel":
            return "steel sword"
        raise Exception("invalid metal bar")
    except Exception as e:
        print(f"An error occurred: {e}")

Instead, the caller should handle any potential error by wrapping the function call within a try/except block.

try:
    craft_sword("gold bar")
except Exception as e:
    print(e)

Assignment

If a player_id that doesn't exist is passed into the get_player_record function, we need to raise (but not handle) our own error to alert the caller of our function that the player they are looking for doesn't exist. The exception should say player id not found.

Note: the tests will call the get_player_record function, and will handle the exception you raise.
"""
"""
Additional notes:
            Bugs           vs        Errors:
-crashes                    | -internet connection lost
-unexpeced behavior         | -expected and handled
-fix the code               | -raise exception
-always bad                 | -throw and return error
-not handling an error      | -alert and tell user 
"""


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")


"""
---------------------------------
Inputs:
 * player_id: 1
Expecting: {'name': 'Slayer', 'level': 128}
Actual: {'name': 'Slayer', 'level': 128}
Pass
---------------------------------
Inputs:
 * player_id: 4
Expecting: player id not found
Actual: player id not found
Pass
---------------------------------
Inputs:
 * player_id: 3
Expecting: {'name': 'Saruman', 'level': 4000}
Actual: {'name': 'Saruman', 'level': 4000}
Pass
---------------------------------
Inputs:
 * player_id: 2
Expecting: {'name': 'Dorgoth', 'level': 300}
Actual: {'name': 'Dorgoth', 'level': 300}
Pass
---------------------------------
Inputs:
 * player_id: 5
Expecting: player id not found
Actual: player id not found
Pass
---------------------------------
Inputs:
 * player_id: 0
Expecting: player id not found
Actual: player id not found
Pass
============= PASS ==============
6 passed, 0 failed
"""