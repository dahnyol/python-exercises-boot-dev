"""
Comparison Operator Evaluations

When a comparison happens, the result of the comparison is just a boolean value, it's either True or False.

Take the following two examples:

is_bigger = 5 > 4

is_bigger = True

In both of the above cases, we're creating a Boolean variable called is_bigger with a value of True.

Because 5 is greater than 4, is_bigger is assigned the value of True.
Assignment

Create the following variables. Use comparison operators to determine their boolean values. The context of the parameter names should tell you how to make these comparisons. Return them in this order:

    is_mustang_edward_same
    is_alphonse_edward_same
    is_winry_alphonse_same
"""

def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = edward_height == mustang_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winery_alphonse_same = winry_height == alphonse_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winery_alphonse_same


"""
---------------------------------
Inputs: 5, 5, 7, 5
Expecting: (True, True, False)   
Actual: (True, True, False)      
Pass
---------------------------------
Inputs: 6, 6, 5, 5
Expecting: (False, True, False)  
Actual: (False, True, False)     
Pass
---------------------------------
Inputs: 4, 4, 4, 4
Expecting: (True, True, True)    
Actual: (True, True, True)       
Pass
---------------------------------
Inputs: 2, 2, 2, 2
Expecting: (True, True, True)    
Actual: (True, True, True)       
Pass
---------------------------------
Inputs: 8, 8, 8, 7
Expecting: (False, True, True)
Actual: (False, True, True)
Pass
---------------------------------
Inputs: 5, 7, 9, 11
Expecting: (False, False, False)
Actual: (False, False, False)
Pass
---------------------------------
Inputs: 11, 9, 7, 5
Expecting: (False, False, False)
Actual: (False, False, False)
Pass
============= PASS ==============
7 passed, 0 failed
"""