"""
Reverse List
Assignment

Some of our players would like to view their inventories in reverse order.

Let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

For example:

[1, 2, 3] -> [3, 2, 1]
['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']

Tip

The Python range function is very useful when working with lists. Alternately, you may want to use list slicing.

    Where should you start your loop from?
    Where should you end your loop?
    What should the step be? In other words, how should you increment i in each iteration of the loop?
"""

# using range
def reverse_array(items):
    reversed_items = []
    for i in range(0, len(items)):
      reversed_items.append(items.pop())
    
    return reversed_items

# using slicing
def reverse_array(items):
    reverse_items = items[::-1]
    return reverse_items

"""
---------------------------------
Input array: ['Shortsword', 'Healing Potion', 'Iron Breastplate', 'Kite Shield']
Expected reversed array: ['Kite Shield', 'Iron Breastplate', 'Healing Potion', 'Shortsword']
Actual reversed array: ['Kite Shield', 'Iron Breastplate', 'Healing Potion', 'Shortsword']
Pass
---------------------------------
Input array: [1, 2, 300, 4, 5]
Expected reversed array: [5, 4, 300, 2, 1]
Actual reversed array: [5, 4, 300, 2, 1]
Pass
---------------------------------
Input array: []
Expected reversed array: []
Actual reversed array: []
Pass
---------------------------------
Input array: ['a']
Expected reversed array: ['a']
Actual reversed array: ['a']
Pass
---------------------------------
Input array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected reversed array: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Actual reversed array: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Pass
---------------------------------
Input array: ['apple', 'banana', 'cherry', 'date', 'elderberry']
Expected reversed array: ['elderberry', 'date', 'cherry', 'banana', 'apple']
Actual reversed array: ['elderberry', 'date', 'cherry', 'banana', 'apple']
Pass
---------------------------------
Input array: ['hello', 'world']
Expected reversed array: ['world', 'hello']
Actual reversed array: ['world', 'hello']
Pass
============= PASS ==============
7 passed, 0 failed
"""