"""
Dictionaries

Dictionaries in Python are used to store data values in key -> value pairs. Dictionaries are a great way to store groups of information.

# use curly braces
# add key-value pairs
car = {
  "brand": "Tesla",
  "model": "3",
  "year": 2019
}

Here the car variable is assigned to a dictionary {} containing the keys brand, model and year. The keys' corresponding values are Tesla, 3 and 2019.
Assignment

Complete the get_character_record function. It takes a character's name, server, level, and rank as individual inputs, and returns a dictionary with the following keys:

    name
    server
    level
    rank
    id

Create and return a dictionary with the input values assigned to the matching keys above. The id key maps to the name and the server inputs concatenated with a # in the middle for uniqueness. We can't have two bloodwarrior123's on the same server!

For example, given:

    name = bloodwarrior123
    server = server1

Then the id field should be set to bloodwarrior123#server1. I recommend using an f-string to create the id field.
"""

def get_character_record(name, server, level, rank):
    character = {
        'name': name,
        'server': server,
        'level': level,
        'rank': rank,
        'id': f"{name}#{server}"
    }
    return character


"""
---------------------------------
Test Case #1

Expected: name: bloodwarrior123
Actual:   name: bloodwarrior123

Expected: server: server1
Actual:   server: server1

Expected: level: 5
Actual:   level: 5

Expected: rank: 1
Actual:   rank: 1

Expected: id: bloodwarrior123#server1
Actual:   id: bloodwarrior123#server1

Pass
---------------------------------
Test Case #2

Expected: name: fronzenboi
Actual:   name: fronzenboi

Expected: server: server2
Actual:   server: server2

Expected: level: 2
Actual:   level: 2

Expected: rank: 1
Actual:   rank: 1

Expected: id: fronzenboi#server2
Actual:   id: fronzenboi#server2

Pass
---------------------------------
Test Case #3

Expected: name: slasher69
Actual:   name: slasher69

Expected: server: server3
Actual:   server: server3

Expected: level: 2
Actual:   level: 2

Expected: rank: 5
Actual:   rank: 5

Expected: id: slasher69#server3
Actual:   id: slasher69#server3

Pass
---------------------------------
Test Case #4

Expected: name: icequeen
Actual:   name: icequeen

Expected: server: server4
Actual:   server: server4

Expected: level: 3
Actual:   level: 3

Expected: rank: 2
Actual:   rank: 2

Expected: id: icequeen#server4
Actual:   id: icequeen#server4

Pass
---------------------------------
Test Case #5

Expected: name: shadowmaster
Actual:   name: shadowmaster

Expected: server: server5
Actual:   server: server5

Expected: level: 4
Actual:   level: 4

Expected: rank: 3
Actual:   rank: 3

Expected: id: shadowmaster#server5
Actual:   id: shadowmaster#server5

Pass
---------------------------------
Test Case #6

Expected: name: silentslasher
Actual:   name: silentslasher

Expected: server: server6
Actual:   server: server6

Expected: level: 5
Actual:   level: 5

Expected: rank: 4
Actual:   rank: 4

Expected: id: silentslasher#server6
Actual:   id: silentslasher#server6

Pass
---------------------------------
Test Case #7

Expected: name: hypershadow
Actual:   name: hypershadow

Expected: server: server7
Actual:   server: server7

Expected: level: 3
Actual:   level: 3

Expected: rank: 5
Actual:   rank: 5

Expected: id: hypershadow#server7
Actual:   id: hypershadow#server7

Pass
============= PASS ==============
7 passed, 0 failed
"""