"""
If Practice

Remember, you can use the == operator to check if two values are equal. For example:

is_equal = 5 == 5
# is_equal is True

Assignment

Complete the check_swords_for_army function. If the number of swords and the number of soldiers match, return the string:

correct amount

Otherwise, return the string:

incorrect amount

Punctuation matters! Make sure you return the strings exactly as they appear above.
"""

def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords == number_of_soldiers:
        return "correct amount"
    return "incorrect amount"


"""
---------------------------------
Inputs: 500, 1000
Expecting: incorrect amount
Actual: incorrect amount
Pass
---------------------------------
Inputs: 800, 800
Expecting: correct amount
Actual: correct amount
Pass
---------------------------------
Inputs: 1500, 1000
Expecting: incorrect amount
Actual: incorrect amount
Pass
---------------------------------
Inputs: 200, 200
Expecting: correct amount
Actual: correct amount
Pass
============= PASS ==============
4 passed, 0 failed
"""