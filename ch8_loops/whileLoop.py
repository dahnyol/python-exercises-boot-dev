"""
While

Python has another type of loop, the while loop. It's a loop that continues while a condition remains True. The syntax is simple:

while 1:
    print("1 evaluates to True")

# prints:
# 1 evaluates to True
# 1 evaluates to True
# (...continuing)

The example above is hardcoded to continue forever, creating an infinite loop. Typically, a while loop condition is a comparison or variable, and it determines when the loop ends:

num = 0
while num < 3:
    num += 1
    print(num)

# prints:
# 1
# 2
# 3
# (the loop stops when num >= 3)

Assignment

In Fantasy Quest, player characters regenerate health when standing still while away from enemies. This means they will gain health but can't run from enemies that are coming towards them while regenerating.

Complete the regenerate function using a while loop. It takes current_health, max_health and enemy_distance integers.

    While regenerating health, a character gains 1 health each iteration until it reaches the max_health amount.
    For every 1 health a character gains, the enemy_distance shortens by 2.
    If an enemy is at a distance of 3 or less from the character, the character stops gaining health.

Return the new current_health after health regeneration stops.
"""

def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2
    return current_health


"""
---------------------------------
Inputs:
 * current_health: 0
 *     max_health: 10
 * enemy_distance: 20
Expecting: 9
   Actual: 9
Pass
---------------------------------
Inputs:
 * current_health: 0
 *     max_health: 10
 * enemy_distance: 4
Expecting: 1
   Actual: 1
Pass
---------------------------------
Inputs:
 * current_health: 8
 *     max_health: 10
 * enemy_distance: 20
Expecting: 10
   Actual: 10
Pass
---------------------------------
Inputs:
 * current_health: 0
 *     max_health: 0
 * enemy_distance: 0
Expecting: 0
   Actual: 0
Pass
---------------------------------
Inputs:
 * current_health: 9
 *     max_health: 10
 * enemy_distance: 3
Expecting: 9
   Actual: 9
Pass
---------------------------------
Inputs:
 * current_health: 100
 *     max_health: 100
 * enemy_distance: 200
Expecting: 100
   Actual: 100
Pass
---------------------------------
Inputs:
 * current_health: 2
 *     max_health: 110
 * enemy_distance: 50
Expecting: 26
   Actual: 26
Pass
---------------------------------
Inputs:
 * current_health: 100
 *     max_health: 1010
 * enemy_distance: 2000
Expecting: 1010
   Actual: 1010
Pass
============= PASS ==============
8 passed, 0 failed
"""