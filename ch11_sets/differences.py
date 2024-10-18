"""
Differences

The Fantasy Quest team merged some of the servers together, but the merge didn't go perfectly. The resulting lists have duplicates and missing ID's. We need to clean up the duplicates and find the missing ids.
Assignment

Complete the find_missing_ids function. It accepts two lists as input, and returns a new list of all the ids present in the first list but not the second. Make sure to remove any duplicates.
Tip

    You can convert a List to a Set using the set() function.
    You can convert a Set to a List using the list() function.
    You can subtract the elements in one Set from another Set using the - operator.

"""

def find_missing_ids(first_ids, second_ids):
    first_ids_set = set(first_ids)
    second_ids_set = set(second_ids)
    merge = first_ids_set - second_ids_set
    return list(merge)


"""
---------------------------------
Inputs: first_ids = [1, 1, 1, 2, 2, 2, 3], second_ids = [1, 2]
Expecting: [3]
Actual: [3]
Pass
---------------------------------
Inputs: first_ids = [1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10], second_ids = [1, 2, 2, 3, 4, 5, 6, 7, 8]
Expecting: [9, 10]
Actual: [9, 10]
Pass
---------------------------------
Inputs: first_ids = [], second_ids = []
Expecting: []
Actual: []
Pass
---------------------------------
Inputs: first_ids = [1, 1, 1], second_ids = []
Expecting: [1]
Actual: [1]
Pass
---------------------------------
Inputs: first_ids = [1, 2, 3, 4, 5], second_ids = [1, 2, 3, 4, 5]
Expecting: []
Actual: []
Pass
---------------------------------
Inputs: first_ids = [1, 1, 2, 2, 3, 3], second_ids = [1, 2, 3]
Expecting: []
Actual: []
Pass
---------------------------------
Inputs: first_ids = [1, 2, 3, 4, 5], second_ids = [1, 2, 3]
Expecting: [4, 5]
Actual: [4, 5]
Pass
---------------------------------
Inputs: first_ids = [1, 2, 3, 4, 5], second_ids = [1, 3, 5]
Expecting: [2, 4]
Actual: [2, 4]
Pass
============= PASS ==============
8 passed, 0 failed
"""