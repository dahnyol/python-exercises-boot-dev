"""
Sets

Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.

fruits = {'apple', 'banana', 'grape'}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}

Add values

fruits = {'apple', 'banana', 'grape'}
fruits.add('pear')
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}

Note: No error will be raised if you add an item already in the set.
Empty set

Because the empty bracket {} syntax creates an empty dictionary, to create an empty set, you need to use the set() function.

fruits = set()
fruits.add('pear')
print(fruits)
# Prints: {'pear'}

Iterate over values in a set (order is not guaranteed)

fruits = {'apple', 'banana', 'grape'}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple

Assignment

Complete the remove_duplicates function. It should take a list of spells that a player has learned and return a new List where there is at most one of each title. You can accomplish this by creating a set, adding all the spells to it, then iterating over the set and adding all the spells into a new List and returning the list.

It makes no sense to learn a spell twice! Once it's learned, it's learned forever.
"""
# using list() function -> creates a list object.
def remove_duplicates(spells):
    # creating a set
    learned_spells = set()
    for spell in spells:
        # adding all the spells to set
        learned_spells.add(spell)
    # adding all the spells into a new List
    return list(learned_spells)

# without using list()
def remove_duplicates(spells):
    # creating a set
    learned_spells = set()
    new_list = []
    for spell in spells:
        # adding all the spells to set
        learned_spells.add(spell)
    # iterating over the set
    for spell in learned_spells:
        # adding all the spells into a new List
        new_list.append(spell)
    # returning the list
    return new_list


"""
---------------------------------
Inputs:
 * spells: ['fireball', 'eldritch blast', 'fireball', 'eldritch blast', 'chill touch', 'eldritch blast', 'chill touch', 'chill touch', 'fireball', 'fireball', 'shocking grasp', 'fireball', 'fireball']
Expecting: ['chill touch', 'eldritch blast', 'fireball', 'shocking grasp']
   Actual: ['eldritch blast', 'chill touch', 'fireball', 'shocking grasp']
Pass
---------------------------------
Inputs:
 * spells: ['fireball', 'fireball', 'fireball']
Expecting: ['fireball']
   Actual: ['fireball']
Pass
---------------------------------
Inputs:
 * spells: ['fireball', 'eldritch blast', 'chill touch', 'shocking grasp']
Expecting: ['chill touch', 'eldritch blast', 'fireball', 'shocking grasp']
   Actual: ['eldritch blast', 'chill touch', 'fireball', 'shocking grasp']
Pass
---------------------------------
Inputs:
 * spells: ['chill touch', 'chill touch', 'chill touch']
Expecting: ['chill touch']
   Actual: ['chill touch']
Pass
---------------------------------
Inputs:
 * spells: ['shocking grasp', 'shocking grasp', 'shocking grasp']
Expecting: ['shocking grasp']
   Actual: ['shocking grasp']
Pass
---------------------------------
Inputs:
 * spells: []
Expecting: []
   Actual: []
Pass
---------------------------------
Inputs:
 * spells: ['eldritch blast', 'eldritch blast', 'eldritch blast']
Expecting: ['eldritch blast']
   Actual: ['eldritch blast']
Pass
============= PASS ==============
7 passed, 0 failed
"""