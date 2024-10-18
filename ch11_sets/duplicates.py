"""
Duplicates

Players are complaining that they aren't able to see their collections easily. Currently every collectible item is displayed, even the duplicates. Players only want to see each artifact once, even if they have collected more than one of them.
Assignment

Complete the remove_duplicates function. It accepts a list of strings and removes any duplicate values. It should utilize and return a set, not a list!

Bonus points if you can write the body of the function in a single line of code.
"""

def remove_duplicates(lst):
    return set(lst)


"""
---------------------------------
Input list: ['Frostmourne', 'Abyssal Whip', 'Staff of Armadyl', 'Frostmourne', 'Abyssal Whip']
Expected set: {'Frostmourne', 'Staff of Armadyl', 'Abyssal Whip'}
Actual set: {'Frostmourne', 'Staff of Armadyl', 'Abyssal Whip'}
Pass
---------------------------------
Input list: ['Ashbringer', 'Dragonfire Shield', 'Serpentine Helm', 'Ashbringer', 'Dragonfire Shield', 'Infinity Boots', 'Serpentine Helm'] 
Expected set: {'Dragonfire Shield', 'Serpentine Helm', 'Ashbringer', 'Infinity Boots'}
Actual set: {'Serpentine Helm', 'Ashbringer', 'Dragonfire Shield', 'Infinity Boots'}
Pass
---------------------------------
Input list: ['Bandos Chestplate', 'Shadowmourne', 'Twisted Bow', 'Bandos Chestplate', 'Shadowmourne', 'Twisted Bow']
Expected set: {'Shadowmourne', 'Bandos Chestplate', 'Twisted Bow'}
Actual set: {'Shadowmourne', 'Bandos Chestplate', 'Twisted Bow'}
Pass
---------------------------------
Input list: []
Expected set: set()
Actual set: set()
Pass
---------------------------------
Input list: ["Zulrah's Scales", "Zulrah's Scales", "Zulrah's Scales"]
Expected set: {"Zulrah's Scales"}
Actual set: {"Zulrah's Scales"}
Pass
---------------------------------
Input list: ['Void Knight Armor', 'Torva Full Helm', 'Void Knight Armor', 'Torva Full Helm']
Expected set: {'Torva Full Helm', 'Void Knight Armor'}
Actual set: {'Torva Full Helm', 'Void Knight Armor'}
Pass
---------------------------------
Input list: ['Abyssal Dagger', 'Armadyl Godsword', 'Bandos Tassets', 'Abyssal Dagger', 'Armadyl Godsword', 'Bandos Tassets']
Expected set: {'Abyssal Dagger', 'Armadyl Godsword', 'Bandos Tassets'}
Actual set: {'Abyssal Dagger', 'Armadyl Godsword', 'Bandos Tassets'}
Pass
---------------------------------
Input list: ['Elysian Spirit Shield', 'Twisted Bow', 'Scythe of Vitur', 'Harmonised Orb', 'Elysian Spirit Shield', 'Twisted Bow', 'Scythe of Vitur', 'Harmonised Orb']
Expected set: {'Harmonised Orb', 'Elysian Spirit Shield', 'Twisted Bow', 'Scythe of Vitur'}
Actual set: {'Harmonised Orb', 'Elysian Spirit Shield', 'Twisted Bow', 'Scythe of Vitur'}
Pass
============= PASS ==============
8 passed, 0 failed
"""