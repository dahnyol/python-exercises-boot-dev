"""
Double the string!

The fantasy quest team wants to add a new easter egg potion to Fantasy Quest! It causes characters to have their in-game chat manipulated when they send messages. The potion doubles every character they send!

    The message they type: Hello there
    The message that is sent: HHeelllloo  tthheerree

Assignment

Complete the double_string function. It takes a string as input and returns a "doubled" version, including spaces!

Example output

sentence = "LF3M BRD full clear"
print(double_string(sentence)) # "LLFF33MM  BBRRDD  ffuullll  cclleeaarr"

Tip

You can iterate over a string as if it were a list of individual characters.

string = "hello world"
for character in string:
    # process individual characters here
"""

def double_string(string):
    char_doubled = ''
    for character in string:
        char_doubled += character + character
    return char_doubled


"""
---------------------------------
Input: Hello there
Expecting: HHeelllloo  tthheerree
Actual: HHeelllloo  tthheerree
Pass
---------------------------------
Input: General Kenobi
Expecting: GGeenneerraall  KKeennoobbii
Actual: GGeenneerraall  KKeennoobbii
Pass
---------------------------------
Input: I am a warrior
Expecting: II  aamm  aa  wwaarrrriioorr
Actual: II  aamm  aa  wwaarrrriioorr
Pass
---------------------------------
Input: Where is the nearest inn?
Expecting: WWhheerree  iiss  tthhee  nneeaarreesstt  iinnnn??
Actual: WWhheerree  iiss  tthhee  nneeaarreesstt  iinnnn??
Pass
---------------------------------
Input: what is happening to my chat?
Expecting: wwhhaatt  iiss  hhaappppeenniinngg  ttoo  mmyy  cchhaatt??
Actual: wwhhaatt  iiss  hhaappppeenniinngg  ttoo  mmyy  cchhaatt??
Pass
---------------------------------
Input: what did this potion do to me?
Expecting: wwhhaatt  ddiidd  tthhiiss  ppoottiioonn  ddoo  ttoo  mmee??
Actual: wwhhaatt  ddiidd  tthhiiss  ppoottiioonn  ddoo  ttoo  mmee??
Pass
============= PASS ==============
6 passed, 0 failed
"""