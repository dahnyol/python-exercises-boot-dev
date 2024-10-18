"""
List Operations - Concatenate

Concatenating two lists (smushing them together) is easy in Python, just use the + operator.

total = [1, 2, 3] + [4, 5, 6]
print(total)
# Prints: [1, 2, 3, 4, 5, 6]

Assignment

Fantasy Quest allows users to keep lists of their favorite items. Your job is to finish the concatenate_favorites function. It takes three different lists - the player's favorite_weapons, favorite_armor and favorite_items.

    Create a new list that combines the lists favorite_weapons, favorite_armor, and favorite_items in this order.
    Return the list containing the combined favorites.

"""

def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    combined = favorite_weapons + favorite_armor + favorite_items
    return combined


"""
---------------------------------
Inputs: ['sword', 'dagger'], ['bracers', 'helmet'], ['feather', 'iron bars']
Expecting: ['sword', 'dagger', 'bracers', 'helmet', 'feather', 'iron bars'] 
Actual: ['sword', 'dagger', 'bracers', 'helmet', 'feather', 'iron bars']    
Pass
---------------------------------
Inputs: ['lance'], ['shield'], ['potions']
Expecting: ['lance', 'shield', 'potions']
Actual: ['lance', 'shield', 'potions']
Pass
---------------------------------
Inputs: ['bow', 'staff'], ['breastplate'], ['scrolls', 'bedroll']
Expecting: ['bow', 'staff', 'breastplate', 'scrolls', 'bedroll']
Actual: ['bow', 'staff', 'breastplate', 'scrolls', 'bedroll']
Pass
---------------------------------
Inputs: [], [], []
Expecting: []
Actual: []
Pass
============= PASS ==============
4 passed, 0 failed
"""