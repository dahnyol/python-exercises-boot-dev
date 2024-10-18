"""
Total Score

The recently added Fantasy Quest battlegrounds are having issues with their in-game score due to how the data is being stored. The first-half score and second-half score are stored in separate dictionaries, making it difficult for them to parse the overall score. You've been asked to write a function that merges the two dictionaries and another function that calculates the total score.
Assignment

Complete the merge and total_score functions.
merge

This function accepts two score dictionaries as input and returns a single merged dictionary that contains all of the keys and values from the input dictionaries.

If a key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary. For example:

two_towers = {"Frodo": "One Ring", "Aragorn": "Narsil"}
rotk = {"Aragorn": "Andúril", "Gandalf": "Glamdring"}
merged_dict = merge(two_towers, rotk)
print(merged_dict)
# {'Frodo': 'One Ring', 'Aragorn': 'Andúril', 'Gandalf': 'Glamdring'}

total_score

This function should take a single score dictionary as input and return the total score calculated from the values of that dictionary.

If no points were scored, the function should return 0.

Don't forget: you can always add print() statements to your code so that you can debug your code before submitting! Print out values of variables to see what's going on, and question your assumptions about what you think is happening.
Example of debugging with print statements

def total_score(score_dict):
    print(f"score_dict: {score_dict}")
    for key in score_dict:
        print(f"key: {key}")

You would then run your code and manually inspect the output to see what's going on. You can always remove the print statements when you're done debugging if you want.
"""

def merge(dict1, dict2):
    merged_dict = {}
    
    for key in dict1:
        merged_dict[key] = dict1[key]
    for key in dict2:
        # If a key exists in both dictionaries, 
        if key in merged_dict:
            # the value from the second dictionary should overwrite the value from the first dictionary.
            merged_dict[key] = key
            
        merged_dict[key] = dict2[key]

    return merged_dict


def total_score(score_dict):
    totalScore = 0
    
    for key in score_dict:
        totalScore += score_dict[key]

    return totalScore


"""
---------------------------------
Inputs:
 * first_half: {'first_quarter': 24, 'second_quarter': 31}
 * second_half: {'third_quarter': 29, 'fourth_quarter': 40}
Expecting: 124
Actual: 124
Pass
---------------------------------
Inputs:
 * first_half: {'first_quarter': 12, 'second_quarter': 2}
 * second_half: {'third_quarter': 32, 'fourth_quarter': 87}
Expecting: 133
Actual: 133
Pass
---------------------------------
Inputs:
 * first_half: {}
 * second_half: {}
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs:
 * first_half: {'first_quarter': 25, 'second_quarter': 2}
 * second_half: {'third_quarter': 31, 'fourth_quarter': 0}
Expecting: 58
Actual: 58
Pass
---------------------------------
Inputs:
 * first_half: {'first_quarter': 25, 'second_quarter': 2}
 * second_half: {'second_quarter': 3, 'third_quarter': 31, 'fourth_quarter': 0}
Expecting: 59
Actual: 59
Pass
---------------------------------
Inputs:
 * first_half: {'first_quarter': 10, 'second_quarter': 20}
 * second_half: {'third_quarter': 30, 'fourth_quarter': 40}
Expecting: 100
Actual: 100
Pass
---------------------------------
Inputs:
 * first_half: {'first_quarter': 15, 'second_quarter': 25}
 * second_half: {'third_quarter': 0, 'fourth_quarter': 0}
Expecting: 40
Actual: 40
Pass
---------------------------------
Inputs:
 * first_half: {'first_quarter': 0, 'second_quarter': 0}
 * second_half: {'third_quarter': 0, 'fourth_quarter': 0}
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs:
 * first_half: {'first_quarter': 100, 'second_quarter': 100}
 * second_half: {'third_quarter': 100, 'fourth_quarter': 100}
Expecting: 400
Actual: 400
Pass
============= PASS ==============
9 passed, 0 failed
"""