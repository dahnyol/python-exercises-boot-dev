"""
List length

The length of a List can be calculated using the len() function.

fruits = ["apple", "banana", "pear"]
length = len(fruits)
# 3

The length of the list is equal to the number of items present. Don't be fooled by the fact that the length is not equal to the index of the last element, in fact, it will always be one greater.
Assignment

Some of our player's inventories are huge, so looking through the entire list is cumbersome. Let's find an easy way for us to get the index of the last item in their inventory.

Complete the get_last_index function so that it returns the length of the inventory list minus 1.
"""

def get_last_index(inventory):
    last_index = len(inventory) - 1
    return last_index


"""
---------------------------------
Inputs: ['Potion']
Expecting: 0
Actual: 0
Pass
---------------------------------     
Inputs: ['Potion', 'Iron Breastplate']
Expecting: 1
Actual: 1
Pass
---------------------------------
Inputs: ['Potion', 'Iron Breastplate', 'Bread', 'Longsword']
Expecting: 3
Actual: 3
Pass
---------------------------------
Inputs: []
Expecting: -1
Actual: -1
Pass
---------------------------------
Inputs: ['Single item']
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs: ['Shield', 'Sword', 'Bow', 'Arrows', 'Health Potion']
Expecting: 4
Actual: 4
Pass
---------------------------------
Inputs: ['Shield', 'Sword', 'Bow']
Expecting: 2
Actual: 2
Pass
---------------------------------
Inputs: ['Shield', 'Sword']
Expecting: 1
Actual: 1
Pass
============= PASS ==============
8 passed, 0 failed
"""