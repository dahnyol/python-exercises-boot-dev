"""
Critical Hit

Barbarian characters in Fantasy Quest have a chance to critically hit when using a flurry attack. If the ability critically hits, then every single attack in the flurry does double damage. A flurry attack's final attack already did double damage to begin with, so if the ability is a critical hit, then the final attack does 4x the damage!
Assignment

In the calculate_flurry_crit function, write a loop that calculates and returns the total_damage of the flurry as a critical hit.

The function takes 2 inputs num_attacks, base_damage.

    Range over the num_attacks for the flurry
    Calculate the total damage for each attack within the flurry. Remember, each attack is a critical hit and does double the base_damage!
    The final swing of the flurry should do 4x the base_damage
    Return the total damage
"""

def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = 0

    for i in range(0, num_attacks):
        if i == num_attacks - 1:
            total_damage += base_damage * 4
        else:
            total_damage += base_damage * 2
    return total_damage


"""
---------------------------------
Num attacks: 2 Base damage: 5
Expecting: 30 damage
Actual: 30 damage
Pass
---------------------------------
Num attacks: 3 Base damage: 15
Expecting: 120 damage
Actual: 120 damage
Pass
---------------------------------
Num attacks: 4 Base damage: 30
Expecting: 300 damage
Actual: 300 damage
Pass
---------------------------------
Num attacks: 1 Base damage: 0
Expecting: 0 damage
Actual: 0 damage
Pass
---------------------------------
Num attacks: 5 Base damage: 50
Expecting: 600 damage
Actual: 600 damage
Pass
---------------------------------
Num attacks: 7 Base damage: 105
Expecting: 1680 damage
Actual: 1680 damage
Pass
---------------------------------
Num attacks: 10 Base damage: 225
Expecting: 4950 damage
Actual: 4950 damage
Pass
---------------------------------
Num attacks: 15 Base damage: 525
Expecting: 16800 damage
Actual: 16800 damage
Pass
---------------------------------
Num attacks: 20 Base damage: 950
Expecting: 39900 damage
Actual: 39900 damage
Pass
============= PASS ==============
9 passed, 0 failed
"""