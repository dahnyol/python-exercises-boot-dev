"""
List Operations - Contains

Checking whether a value exists in a list is also really easy in Python, just use the in keyword.

fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True

Assignment

Our players have requested an in-game feature that will allow them to type in a weapon name to check if it's in the list of top weapons in the realm.

Complete the is_top_weapon function. It should return True if the weapon is in the top_weapons list, otherwise it should return False.
"""

def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    # don't touch above this line
    return weapon in top_weapons


"""
---------------------------------
Input:
 * Weapon: sword of justice
Expecting: True
Actual: True
Pass
---------------------------------
Input:
 * Weapon: bronze mace
Expecting: False
Actual: False
Pass
---------------------------------
Input:
 * Weapon: sword of slashing
Expecting: True
Actual: True
Pass
---------------------------------
Input:
 * Weapon:
Expecting: False
Actual: False
Pass
---------------------------------
Input:
 * Weapon: great axe
Expecting: True
Actual: True
Pass
---------------------------------
Input:
 * Weapon: silver bow
Expecting: True
Actual: True
Pass
---------------------------------
Input:
 * Weapon: golden spear
Expecting: False
Actual: False
Pass
---------------------------------
Input:
 * Weapon: spiked knuckles
Expecting: True
Actual: True
Pass
---------------------------------
Input:
 * Weapon: spellbook
Expecting: True
Actual: True
Pass
============= PASS ==============
9 passed, 0 failed
"""