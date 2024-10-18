"""
List Updates

We can also change the item that exists at a given index. For example, we can change Leather to Leather Armor in the inventory list in the following way:

inventory = ["Leather", "Iron Ore", "Healing Potion"]
inventory[0] = "Leather Armor"
# inventory: ['Leather Armor', 'Iron Ore', 'Healing Potion']

Assignment

Fantasy Quest is trialling a new inventory system for their hardcore game mode. If a player has Iron Ore or an Iron Bar, it is always stored in the 2nd inventory slot (and they can only have one or the other).

Let's finish the smelt_ore function. When a player tries to smelt Iron Ore we need to change it into an Iron Bar, but only if they already have Iron Ore in their inventory slot.
"""

def smelt_ore(inventory):
    if inventory[1] == 'Iron Ore':
        inventory[1] = 'Iron Bar'

    return inventory


"""
---------------------------------
Inputs: ['Potion', 'Iron Bar', 'Iron Sword', 'Leather Armor']
Expecting: ['Potion', 'Iron Bar', 'Iron Sword', 'Leather Armor']
Actual: ['Potion', 'Iron Bar', 'Iron Sword', 'Leather Armor']
Pass
---------------------------------
Inputs: ['Potion', 'Iron Ore', None, None]
Expecting: ['Potion', 'Iron Bar', None, None]
Actual: ['Potion', 'Iron Bar', None, None]
Pass
---------------------------------
Inputs: [None, None, None, None]
Expecting: [None, None, None, None]
Actual: [None, None, None, None]
Pass
---------------------------------
Inputs: [None, 'Iron Ore', None, 'Leather Armor']
Expecting: [None, 'Iron Bar', None, 'Leather Armor']
Actual: [None, 'Iron Bar', None, 'Leather Armor']
Pass
============= PASS ==============
4 passed, 0 failed
"""