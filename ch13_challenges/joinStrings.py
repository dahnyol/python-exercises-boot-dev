"""
Join Strings

Write a function called join_strings() that takes a list of strings and returns a single string. Concatenate the strings from the list end-to-end, in order, with a comma between them. Don't use the .join() string method.
Example

string_list = ["hello", "my", "friend"]
joined_string = join_strings(string_list)
print(joined_string) # "hello,my,friend"

Tip

You don't want a comma at the beginning or the end of the final string!
"""

def join_strings(strings):
    joined_string = ''

    for i in range(len(strings)):
        # concat the current word to the join_string var
        joined_string += strings[i]
        # check if the current word is the last in the strings list
        # if it is not the last element, concat a comma to join_string var
        if i != len(strings) - 1:
            joined_string += ','
   
    return joined_string


"""
---------------------------------
Input: ['hello', 'world']
Expecting: hello,world
Actual: hello,world
Pass
---------------------------------
Input: ['this', 'list', 'is', 'so', 'important']
Expecting: this,list,is,so,important
Actual: this,list,is,so,important
Pass
---------------------------------
Input: []
Expecting:
Actual:
Pass
---------------------------------
Input: ['ford', 'ferrari', 'tesla']
Expecting: ford,ferrari,tesla
Actual: ford,ferrari,tesla
Pass
---------------------------------
Input: ['musk', 'satya', 'cook', 'bezos']
Expecting: musk,satya,cook,bezos
Actual: musk,satya,cook,bezos
Pass
---------------------------------
Input: ['dota', 'sc2', 'overwatch', 'diablo', 'mtg']
Expecting: dota,sc2,overwatch,diablo,mtg
Actual: dota,sc2,overwatch,diablo,mtg
Pass
============= PASS ==============
6 passed, 0 failed
"""