"""
Race

Rogue characters in Fantasy Quest expend energy when they sprint. Tyler is trying to figure out if his rogue has enough energy to get him from the inn to the capital city and back to the inn. He needs to go to the capital to pay his yearly income tax, but wants to return to the inn because it has a complimentary continental breakfast.
Assignment

Complete the has_enough_energy function.

Do some Pythonic math with the distance_one_way and meters_per_energy variables to determine how many points of energy are needed for Tyler to get to the capital city AND make it back to the inn. Assign the result to a energy_needed variable. distance_one_way is how many meters it is to get from here to there. meters_per_energy is how far Tyler's rogue can travel with one energy point.

Return True if there is at least enough energy based on the energy_needed variable, and False otherwise.
Hint

    If you travel distance_one_way from point A to point B, you will have to travel that same distance again to get back to point A.
"""

def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    distance = distance_one_way * 2
    energy_needed = distance / meters_per_energy 
    if energy_available >= energy_needed:
        return True
    return False


"""
---------------------------------
Inputs: 8, 50, 22
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 9, 100, 20
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 10, 50, 18
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 3, 105, 22
Expecting: False
Actual: False
Pass
---------------------------------
Inputs: 1, 1, 2
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 2, 1, 1
Expecting: True
Actual: True
Pass
---------------------------------
Inputs: 1, 2, 1
Expecting: False
Actual: False
Pass
============= PASS ==============
7 passed, 0 failed
"""