"""
Should Serve Drinks
Assignment

In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!

Complete the function that determines if a bartender should serve drinks to a customer. Only return True if all of these conditions apply, else return False:

    The customer's age is 21 or older
    The bartender is working
    The time is at least 5 but no later than 10

Tip - If statements don't need a comparison

Where "is_big" is a boolean value, the following statements are identical:

if is_big:
    # ...

if is_big == True:
    # ...

The first option should be preferred due to length; however, the second is more readable. The == True is redundant.
"""

def should_serve_customer(customer_age, on_break, time):
    if customer_age >= 21 and on_break == False and time >= 5 and time <= 10:
        return True
    return False


"""
---------------------------------
Inputs:
 * customer_age: 22
 * on_break: False
 * time: 10
Expecting: True
Actual: True
Pass
---------------------------------
Inputs:
 * customer_age: 41
 * on_break: False
 * time: 1
Expecting: False
Actual: False
Pass
---------------------------------
Inputs:
 * customer_age: 14
 * on_break: False
 * time: 7
Expecting: False
Actual: False
Pass
---------------------------------
Inputs:
 * customer_age: 21
 * on_break: False
 * time: 5
Expecting: True
Actual: True
Pass
---------------------------------
Inputs:
 * customer_age: 107
 * on_break: False
 * time: 9
Expecting: True
Actual: True
Pass
---------------------------------
Inputs:
 * customer_age: 23
 * on_break: True
 * time: 5
Expecting: False
Actual: False
Pass
---------------------------------
Inputs:
 * customer_age: 21
 * on_break: False
 * time: 4
Expecting: False
Actual: False
Pass
---------------------------------
Inputs:
 * customer_age: 57
 * on_break: False
 * time: 11
Expecting: False
Actual: False
Pass
---------------------------------
Inputs:
 * customer_age: 20
 * on_break: False
 * time: 5
Expecting: False
Actual: False
Pass
============= PASS ==============
9 passed, 0 failed
"""