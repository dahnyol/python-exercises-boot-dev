"""
Iterating over a dictionary in Python

We can iterate over a dictionary's keys using the same no-index syntax we used to iterate over the values in a list. With access to the dictionary's keys, we also have access to their corresponding values.

fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny

Note: we could have just as easily set the name variable to key or simply k.
Assignment

We need to display on our player's screens what the most common enemy in a given area of the game map is.

Complete the get_most_common_enemy function by iterating over all enemies in the dictionary and returning only the name of the enemy with the highest count.

If there are no enemies, return None. If there are multiple enemies with the same highest count, return the first one found.

enemies_dict is a dictionary of name -> count.
Tip: Negative infinity

When you're trying to find a "max" value, it helps to keep track of the "max so far" in a variable and to start that variable at the lowest possible number, negative infinity.

max_so_far = float("-inf")

You'll also want to keep track of the enemy name associated with the maximum count. I would set the default for that variable to None.
"""

def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    enemy_name = None

    for name in enemies_dict:
        count = enemies_dict[name]
        if count > max_so_far:
            max_so_far = count
            enemy_name = name
    return enemy_name

"""
---------------------------------
Inputs: {'jackal': 4, 'kobold': 3, 'soldier': 10, 'gremlin': 5}
Expecting: soldier
Actual: soldier
Pass
---------------------------------
Inputs: {'jackal': 1, 'kobold': 3, 'soldier': 2, 'gremlin': 5}
Expecting: gremlin
Actual: gremlin
Pass
---------------------------------
Inputs: {'jackal': 2, 'gremlin': 7}
Expecting: gremlin
Actual: gremlin
Pass
---------------------------------
Inputs: {'jackal': 3}
Expecting: jackal
Actual: jackal
Pass
---------------------------------
Inputs: {}
Expecting: None
Actual: None
Pass
---------------------------------
Inputs: {'kobold': 5, 'soldier': 5, 'gremlin': 5, 'dragon': 5}
Expecting: kobold
Actual: kobold
Pass
---------------------------------
Inputs: {'jackal': 5, 'kobold': 3, 'soldier': 10, 'gremlin': 5, 'dragon': 20}
Expecting: dragon
Actual: dragon
Pass
---------------------------------
Inputs: {'jackal': 5, 'kobold': 3, 'soldier': 2, 'gremlin': 10, 'dragon': 1}
Expecting: gremlin
Actual: gremlin
Pass
============= PASS ==============
8 passed, 0 failed
"""