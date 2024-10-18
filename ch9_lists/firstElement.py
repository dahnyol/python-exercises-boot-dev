"""
First Element
Assignment

Let's add another function to our inventory system. Write a function that returns the first element from a list. If the list is empty then return the string ERROR instead.
"""

def get_first_item(items):
    if len(items) < 1:
        return 'ERROR'
    return items[0]


"""
---------------------------------
Input: [1, 2]
Expecting: 1
Actual: 1
Pass
---------------------------------
Input: ['Healing Potion']
Expecting: Healing Potion
Actual: Healing Potion
Pass
---------------------------------
Input: []
Expecting: ERROR
Actual: ERROR
Pass
---------------------------------
Input: ['Iron Ore', 'Iron Bar', 'Scimitar']
Expecting: Iron Ore
Actual: Iron Ore
Pass
---------------------------------
Input: ['Apple', 'Banana', 'Cherry']
Expecting: Apple
Actual: Apple
Pass
---------------------------------
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Expecting: [1, 2, 3]
Actual: [1, 2, 3]
Pass
---------------------------------
Input: [False, True, False]
Expecting: False
Actual: False
Pass
---------------------------------
Input: [None, 'None', 0]
Expecting: None
Actual: None
Pass
============= PASS ==============
8 passed, 0 failed
"""