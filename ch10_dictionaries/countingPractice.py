"""
Counting Practice
Checking for existence

If you're unsure whether or not a key exists in a dictionary, use the in keyword.

cars = {
    "ford": "f150",
    "tesla": "3"
}

print("ford" in cars)
# Prints: True

print("gmc" in cars)
# Prints: False

Assignment

We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind. Fix the count_enemies function. If you run the code, it will result in a KeyError. It takes a list of enemy_names as input. It should return a dictionary where the keys are all the enemy names from the list, and the values are the counts of how many times each enemy appeared in the list.
"""

def count_enemies(enemy_names):
    enemies_dict = {}

    for enemy_name in enemy_names:
        # check if the name already exists in the enemies_dict
        if enemy_name in enemies_dict:
            # name already exists in the dict? increment 1
            enemies_dict[enemy_name] += 1
        else:
            # doesn't exist enemies_dict, initalize key with the enemy_name, with the value 1
            enemies_dict[enemy_name] = 1
            
    return enemies_dict


"""
---------------------------------
Inputs: ['jackal', 'kobold', 'soldier']
Expecting: {'jackal': 1, 'kobold': 1, 'soldier': 1}
Actual: {'jackal': 1, 'kobold': 1, 'soldier': 1}
Pass
---------------------------------
Inputs: ['jackal', 'kobold', 'jackal']
Expecting: {'jackal': 2, 'kobold': 1}
Actual: {'jackal': 2, 'kobold': 1}
Pass
---------------------------------
Inputs: []
Expecting: {}
Actual: {}
Pass
---------------------------------
Inputs: ['jackal']
Expecting: {'jackal': 1}
Actual: {'jackal': 1}
Pass
---------------------------------
Inputs: ['jackal', 'kobold', 'jackal', 'kobold', 'soldier', 'kobold', 'soldier', 'soldier', 'jackal', 'jackal', 'gremlin', 'jackal', 'jackal']
Expecting: {'jackal': 6, 'kobold': 3, 'soldier': 3, 'gremlin': 1}
Actual: {'jackal': 6, 'kobold': 3, 'soldier': 3, 'gremlin': 1}
Pass
---------------------------------
Inputs: ['jackal', 'kobold', 'gremlin']
Expecting: {'jackal': 1, 'kobold': 1, 'gremlin': 1}
Actual: {'jackal': 1, 'kobold': 1, 'gremlin': 1}
Pass
---------------------------------
Inputs: ['jackal', 'jackal', 'jackal']
Expecting: {'jackal': 3}
Actual: {'jackal': 3}
Pass
---------------------------------
Inputs: ['gremlin', 'gremlin', 'gremlin']
Expecting: {'gremlin': 3}
Actual: {'gremlin': 3}
Pass
============= PASS ==============
8 passed, 0 failed
"""