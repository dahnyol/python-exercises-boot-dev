"""
Meditate

In Fantasy Quest, player characters have spells and abilities that cost mana to cast. Characters can meditate to regenerate mana by converting energy directly into mana. Energy potions can be used to instantly regain energy.
Assignment

Complete the meditate function using a while loop. It takes mana, max_mana, energy and energy_potions integers.

    While meditating, a character converts 1 energy into at most 3 mana — their mana cannot exceed their max mana — for each iteration of the loop.
    mana cannot exceed the max_mana.
    If they have any energy_potions when they run out of energy, they will use 1 energy potion to gain 50 energy and continue meditating.
    A character will stop meditating if either:
        Their mana reaches the max_mana, or
        They run out of energy and energy_potions.

Return the mana and remaining energy and energy_potions when the character stops meditating.
Tip

Don't forget! A character cannot have more mana than their max_mana threshold. Be sure to handle cases where meditate raises their mana above their max.
"""

def meditate(mana, max_mana, energy, energy_potions):
    while mana < max_mana and (energy > 0 or energy_potions > 0):
        if energy == 0 and energy_potions > 0:
            energy_potions -= 1
            energy += 50
        
        if energy > 0:
            mana_gained = min(3, max_mana - mana)
            mana += mana_gained
            energy -= 1

    return mana, energy, energy_potions


"""
---------------------------------
Inputs:
 *           mana: 0
 *       max_mana: 10
 *         energy: 3
 * energy_potions: 0
Expecting: mana 9, energy 0, energy potions 0
   Actual: mana 9, energy 0, energy potions 0
Pass
---------------------------------
Inputs:
 *           mana: 0
 *       max_mana: 12
 *         energy: 0
 * energy_potions: 1
Expecting: mana 12, energy 46, energy potions 0
   Actual: mana 12, energy 46, energy potions 0
Pass
---------------------------------
Inputs:
 *           mana: 1
 *       max_mana: 100
 *         energy: 33
 * energy_potions: 2
Expecting: mana 100, energy 0, energy potions 2
   Actual: mana 100, energy 0, energy potions 2
Pass
---------------------------------
Inputs:
 *           mana: 0
 *       max_mana: 0
 *         energy: 0
 * energy_potions: 0
Expecting: mana 0, energy 0, energy potions 0
   Actual: mana 0, energy 0, energy potions 0
Pass
---------------------------------
Inputs:
 *           mana: 1000
 *       max_mana: 1000
 *         energy: 200
 * energy_potions: 5
Expecting: mana 1000, energy 200, energy potions 5
   Actual: mana 1000, energy 200, energy potions 5
Pass
---------------------------------
Inputs:
 *           mana: 0
 *       max_mana: 10
 *         energy: 0
 * energy_potions: 2
Expecting: mana 10, energy 46, energy potions 1
   Actual: mana 10, energy 46, energy potions 1
Pass
---------------------------------
Inputs:
 *           mana: 5
 *       max_mana: 2000
 *         energy: 200
 * energy_potions: 3
Expecting: mana 1055, energy 0, energy potions 0
   Actual: mana 1055, energy 0, energy potions 0
Pass
============= PASS ==============
7 passed, 0 failed
"""