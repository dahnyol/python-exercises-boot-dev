"""
Alchemy Ingredients

Fantasy Quest added a new alchemy profession, users would like a way to know how many correctly ordered ingredients they have compared to the required ingredients in their recipes.
Assignment

Finish the check_ingredient_match function by looping over the recipe list. The function should calculate and return a percentage of ingredients the character has, as well as a list of missing or wrongly ordered ingredients from the recipe.

The order of the ingredients matter! They must be in the same index as the recipe to match. The missing ingredients must also be in the same order as they appear in the recipe list.

For example, if these were the lists:

recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
ingredients = ["Dragon Scale", "Goblin Ear", "Phoenix Feather", "Troll Tusk"]

percentage, missing_ingredients = check_ingredient_match(recipe, ingredients)
print(percentage, missing_ingredients)
# Prints: 75.00 ["Unicorn Hair"]

The percentage must be a float, not an integer!
"""

def check_ingredient_match(recipe, ingredients):
    missing_ingredient = []
    counter = 0
    
    for i in range(0, len(recipe)):
        if recipe[i] != ingredients[i]:
            missing_ingredient.append(recipe[i])
        else:
            counter += 1

    percentage = (counter / len(recipe)) * 100          

    return percentage, missing_ingredient


"""
---------------------------------
Inputs:
recipe: ['Dragon Scale', 'Unicorn Hair', 'Phoenix Feather', 'Troll Tusk', 'Mandrake Root', 'Griffin Feather', 'Elf Dust', 'Goblin Ear']    
gathered_ingredients: ['Dragon Scale', 'Goblin Ear', 'Phoenix Feather', 'Elf Dust', 'Mandrake Root', 'Griffin Feather', 'Elf Dust', 'Goblin Ear']
Expecting: (75.0, ['Unicorn Hair', 'Troll Tusk'])
Actual: (75.0, ['Unicorn Hair', 'Troll Tusk'])
Pass
---------------------------------
Inputs:
recipe: ['Dragon Scale', 'Unicorn Hair', 'Phoenix Feather', 'Troll Tusk', 'Mandrake Root', 'Griffin Feather', 'Elf Dust']
gathered_ingredients: ['Dragon Scale', 'Unicorn Hair', 'Phoenix Feather', 'Troll Tusk', 'Mandrake Root', 'Griffin Feather', 'Elf Dust']    
Expecting: (100.0, [])
Actual: (100.0, [])
Pass
---------------------------------
Inputs:
recipe: ['Dragon Scale', 'Unicorn Hair', 'Phoenix Feather', 'Troll Tusk', 'Mandrake Root', 'Griffin Feather', 'Elf Dust']
gathered_ingredients: ['Goblin Ear', 'Elf Dust', 'Griffin Feather', 'Mermaid Tear', 'Goblin Ear', 'Phoenix Feather', 'Troll Tusk']
Expecting: (0.0, ['Dragon Scale', 'Unicorn Hair', 'Phoenix Feather', 'Troll Tusk', 'Mandrake Root', 'Griffin Feather', 'Elf Dust'])        
Actual: (0.0, ['Dragon Scale', 'Unicorn Hair', 'Phoenix Feather', 'Troll Tusk', 'Mandrake Root', 'Griffin Feather', 'Elf Dust'])
Pass
---------------------------------
Inputs:
recipe: ['Dragon Scale', 'Unicorn Hair', 'Phoenix Feather', 'Troll Tusk', 'Mandrake Root', 'Griffin Feather', 'Elf Dust', 'Goblin Ear']    
gathered_ingredients: ['Unicorn Hair', 'Dragon Scale', 'Phoenix Feather', 'Troll Tusk', 'Griffin Feather', 'Mandrake Root', 'Goblin Ear', 'Elf Dust']
Expecting: (25.0, ['Dragon Scale', 'Unicorn Hair', 'Mandrake Root', 'Griffin Feather', 'Elf Dust', 'Goblin Ear'])
Actual: (25.0, ['Dragon Scale', 'Unicorn Hair', 'Mandrake Root', 'Griffin Feather', 'Elf Dust', 'Goblin Ear'])
Pass
============= PASS ==============
4 passed, 0 failed
"""