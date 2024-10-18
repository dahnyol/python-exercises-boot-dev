"""
Find an item in a list

Example of "no-index" or "no-range" syntax:

for fruit in fruits:
    print(fruit)

Assignment

We need to check if a player has a specific item in their inventory. In the contains_leather_scraps function, use the no-index syntax to iterate over each item in items. If you find an item called Leather Scraps, set the found variable to True.
"""

def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if item == 'Leather Scraps':
            found = True

    # don't touch below this line

    return found


"""
---------------------------------
Inputs: ['Potion', 'Healing Potion', 'Iron Breastplate', 'Leather Scraps']
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: ['Potion', 'Shortsword', 'Buckler', 'Iron Mace']
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: []
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: ['Leather Scraps']
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: ['Potion', 'Leather Scraps', 'Leather Scraps']
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: ['Potion', 'Healing Potion']
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: ['Leather scraps']
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: ['Leather', 'Scraps']
Expecting: False
Actual: False
Pass
============= PASS ==============
8 passed, 0 failed
"""