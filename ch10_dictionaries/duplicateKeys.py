"""
Duplicate Keys

Because dictionaries rely on unique keys, you can't have two of the same key in the same dictionary. If you try to use the same key twice, the first value will simply be overwritten.
Assignment

Another developer on our team has introduced a bug by specifying duplicate keys in the dictionary! Fix the bug.

The get_character_record function takes a character's name, server, level, and rank. It should return a dictionary with the following fields:

    name
    server
    level
    rank
    id

Where the id is the name and the server concatenated together with a # in the middle for uniqueness. We can't have two bloodwarrior123's on the same server!
"""

def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }


"""
---------------------------------
Inputs: bloodwarrior123, server1, 5, 1
Expecting: {'name': 'bloodwarrior123', 'server': 'server1', 'level': 5, 'rank': 1, 'id': 'bloodwarrior123#server1'}
Actual: {'name': 'bloodwarrior123', 'server': 'server1', 'level': 1, 'rank': 2, 'id': 'bloodwarrior123#server1'}
Fail
---------------------------------
Inputs: fronzenboi, server2, 2, 1
Expecting: {'name': 'fronzenboi', 'server': 'server2', 'level': 2, 'rank': 1, 'id': 'fronzenboi#server2'}
Actual: {'name': 'fronzenboi', 'server': 'server2', 'level': 1, 'rank': 2, 'id': 'fronzenboi#server2'}
Fail
---------------------------------
Inputs: slasher69, server3, 2, 5
Expecting: {'name': 'slasher69', 'server': 'server3', 'level': 2, 'rank': 5, 'id': 'slasher69#server3'}
Actual: {'name': 'slasher69', 'server': 'server3', 'level': 1, 'rank': 2, 'id': 'slasher69#server3'}
Fail
Inputs: kingofgames, server4, 3, 2
Expecting: {'name': 'kingofgames', 'server': 'server4', 'level': 3, 'rank': 2, 'id': 'kingofgames#server4'}
Actual: {'name': 'kingofgames', 'server': 'server4', 'level': 1, 'rank': 2, 'id': 'kingofgames#server4'}
Fail
---------------------------------
Inputs: godofwar, server5, 1, 5
Expecting: {'name': 'godofwar', 'server': 'server5', 'level': 1, 'rank': 5, 'id': 'godofwar#server5'}
Actual: {'name': 'godofwar', 'server': 'server5', 'level': 1, 'rank': 2, 'id': 'godofwar#server5'}
Fail
---------------------------------
Inputs: pythonista, server6, 4, 3
Expecting: {'name': 'pythonista', 'server': 'server6', 'level': 4, 'rank': 3, 'id': 'pythonista#server6'}
Actual: {'name': 'pythonista', 'server': 'server6', 'level': 1, 'rank': 2, 'id': 'pythonista#server6'}
Fail
---------------------------------
Inputs: codemaster, server7, 3, 1
Expecting: {'name': 'codemaster', 'server': 'server7', 'level': 3, 'rank': 1, 'id': 'codemaster#server7'}
Actual: {'name': 'codemaster', 'server': 'server7', 'level': 1, 'rank': 2, 'id': 'codemaster#server7'}
Fail
============= FAIL ==============
0 passed, 7 failed
PS C:\Users\Daniel\Documents\boot-dev-lessons\python-exercises> & C:/Users/Daniel/AppData/Local/Programs/Python/Python313/python.exe c:/Users/Daniel/Documents/boot-dev-lessons/python-exercises/ch10_dictionaries/duplicateKeys_test.py
---------------------------------
Inputs: bloodwarrior123, server1, 5, 1
Expecting: {'name': 'bloodwarrior123', 'server': 'server1', 'level': 5, 'rank': 1, 'id': 'bloodwarrior123#server1'}
Actual: {'name': 'bloodwarrior123', 'server': 'server1', 'level': 5, 'rank': 1, 'id': 'bloodwarrior123#server1'}
Pass
---------------------------------
Inputs: fronzenboi, server2, 2, 1
Expecting: {'name': 'fronzenboi', 'server': 'server2', 'level': 2, 'rank': 1, 'id': 'fronzenboi#server2'}
Actual: {'name': 'fronzenboi', 'server': 'server2', 'level': 2, 'rank': 1, 'id': 'fronzenboi#server2'}
Pass
---------------------------------
Inputs: slasher69, server3, 2, 5
Expecting: {'name': 'slasher69', 'server': 'server3', 'level': 2, 'rank': 5, 'id': 'slasher69#server3'}
Actual: {'name': 'slasher69', 'server': 'server3', 'level': 2, 'rank': 5, 'id': 'slasher69#server3'}
Pass
---------------------------------
Inputs: kingofgames, server4, 3, 2
Expecting: {'name': 'kingofgames', 'server': 'server4', 'level': 3, 'rank': 2, 'id': 'kingofgames#server4'}
Actual: {'name': 'kingofgames', 'server': 'server4', 'level': 3, 'rank': 2, 'id': 'kingofgames#server4'}
Pass
---------------------------------
Inputs: godofwar, server5, 1, 5
Expecting: {'name': 'godofwar', 'server': 'server5', 'level': 1, 'rank': 5, 'id': 'godofwar#server5'}
Actual: {'name': 'godofwar', 'server': 'server5', 'level': 1, 'rank': 5, 'id': 'godofwar#server5'}
Pass
---------------------------------
Inputs: pythonista, server6, 4, 3
Expecting: {'name': 'pythonista', 'server': 'server6', 'level': 4, 'rank': 3, 'id': 'pythonista#server6'}
Actual: {'name': 'pythonista', 'server': 'server6', 'level': 4, 'rank': 3, 'id': 'pythonista#server6'}
Pass
---------------------------------
Inputs: codemaster, server7, 3, 1
Expecting: {'name': 'codemaster', 'server': 'server7', 'level': 3, 'rank': 1, 'id': 'codemaster#server7'}
Actual: {'name': 'codemaster', 'server': 'server7', 'level': 3, 'rank': 1, 'id': 'codemaster#server7'}
Pass
============= PASS ==============
7 passed, 0 failed
"""