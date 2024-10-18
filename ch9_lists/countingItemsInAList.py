"""
Counting the items in a list

Remember that we can iterate over all the elements in a list using a loop. For example, the following code will print each item in the sports list.

for i in range(0, len(sports)):
    print(sports[i])

Assignment

Our players need a way to see how many copies of a specific item they have within their inventory!

Let's finish the get_item_counts function. Within the loop, check if the items are a Potion, Bread, or Shortsword, then add up how many there are of each by incrementing the potion_count, bread_count and shortsword_count variables respectively.
Tip

The example shows you how to access the values in a list. Combine this with what you know about comparison and assignment operators to complete the assignment.
"""

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        if items[i] == 'Potion':
            potion_count += 1
        if items[i] == 'Bread':
            bread_count += 1
        if items[i] == 'Shortsword':
            shortsword_count += 1
    # don't touch below this line

    return potion_count, bread_count, shortsword_count


"""
---------------------------------
Inputs: ['Bread', 'Potion', 'Shortsword', 'Bread']
Expecting: (1, 2, 1)
Actual: (1, 2, 1)
Pass
---------------------------------
Inputs: ['Potion', 'Potion', 'Shortsword', 'Buckler', 'Iron Mace']
Expecting: (2, 0, 1)
Actual: (2, 0, 1)
Pass
---------------------------------
Inputs: []
Expecting: (0, 0, 0)
Actual: (0, 0, 0)
Pass
---------------------------------
Inputs: ['Potion', 'Leather Scraps', 'Bread', 'Iron Ore', 'Light Leather', 'Bread', 'Shortsword', 'Longsword', 'Ironwood Branch', 'Shortsword', 'Shortsword']
Expecting: (1, 2, 3)
Actual: (1, 2, 3)
Pass
---------------------------------
Inputs: ['Bread', 'Bread', 'Bread', 'Bread']
Expecting: (0, 4, 0)
Actual: (0, 4, 0)
Pass
---------------------------------
Inputs: ['Shortsword', 'Shortsword', 'Shortsword', 'Shortsword']
Expecting: (0, 0, 4)
Actual: (0, 0, 4)
Pass
---------------------------------
Inputs: ['Potion']
Expecting: (1, 0, 0)
Actual: (1, 0, 0)
Pass
---------------------------------
Inputs: ['Potion', 'Bread', 'Shortsword']
Expecting: (1, 1, 1)
Actual: (1, 1, 1)
Pass
============= PASS ==============
8 passed, 0 failed
"""