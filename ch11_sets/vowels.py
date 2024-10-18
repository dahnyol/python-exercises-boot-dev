"""
Vowels

You've been hired by a blogging company and they are asking you to analyze one of their recent posts to determine the number of vowels present in their paragraphs.
Assignment

Complete the count_vowels function. It should take a string and return a count of the number of vowels within the given string, and a set of its unique vowels.
Tip

For this challenge, we are only interested in the 5 vowels: a, e, i, o, u, and their capitalized versions. In addition, treat uppercase and lowercase vowels as separate. For example, "A" and "a" are not the same.
"""
# 'a','e','i','o','u','A','E','I','O','U'
def count_vowels(text):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    unique_vowels = set()

    for char in text:
        if char in vowels:
            count += 1
            unique_vowels.add(char)

    return count, unique_vowels    


"""
---------------------------------
Inputs:
 * Text: Did someone say Thunderfury, Blessed Blade of the Windseeker?
Expecting: (19, {'e', 'i', 'o', 'a', 'u'})
19 {'i', 'o', 'u', 'e', 'a'}
Actual: (19, {'i', 'o', 'u', 'e', 'a'})
Pass
---------------------------------
Inputs:
 * Text: LF9M UBRS NEED ALL!!!!
Expecting: (4, {'U', 'E', 'A'})
4 {'U', 'E', 'A'}
Actual: (4, {'U', 'E', 'A'})
Pass
---------------------------------
Inputs:
 * Text: Leatherworker LFW Have all end game recipes!
Expecting: (14, {'e', 'i', 'o', 'a'})
14 {'e', 'i', 'o', 'a'}
Actual: (14, {'e', 'i', 'o', 'a'})
Pass
---------------------------------
Inputs:
 * Text:
Expecting: (0, set())
0 set()
Actual: (0, set())
Pass
---------------------------------
Inputs:
 * Text: Can anyone spare 1g so I can train my new spells?
Expecting: (13, {'e', 'i', 'I', 'o', 'a'})
13 {'i', 'I', 'o', 'e', 'a'}
Actual: (13, {'i', 'I', 'o', 'e', 'a'})
Pass
---------------------------------
Inputs:
 * Text: no
Expecting: (1, {'o'})
1 {'o'}
Actual: (1, {'o'})
Pass
---------------------------------
Inputs:
 * Text: mages need a nerf
Expecting: (6, {'e', 'a'})
6 {'e', 'a'}
Actual: (6, {'e', 'a'})
Pass
---------------------------------
Inputs:
 * Text: wtb port to Roshar
Expecting: (4, {'o', 'a'})
4 {'o', 'a'}
Actual: (4, {'o', 'a'})
Pass
============= PASS ==============
8 passed, 0 failed
"""