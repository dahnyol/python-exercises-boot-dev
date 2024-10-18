"""
Different types of exceptions

We haven't covered classes and objects yet, which is what an Exception really is at its core. We'll go more into that in the course on object-oriented programming.

For now, what is important to understand is that there are different types of exceptions and we can handle them differently depending on the situation. Some exceptions are more specific, like ZeroDivisionError or IndexError, and some are more general, like the base Exception.
Syntax

try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)

Which will print:

0 division
index error

Why specific exceptions come first

When handling exceptions, it’s important to catch the most specific ones first, because Python stops checking once it finds a matching exception handler. If you catch a more general Exception first, any specific errors will never get handled individually.

For example:

try:
    nums = [0, 1]
    print(nums[2])
except Exception:
    print("An error occurred")
except IndexError:
    print("Index error")

In this case, the general Exception will catch the error before the IndexError can be reached, and the message “Index error” will never be printed. Always handle the most specific exception first!
Alias exception messages

As seen in the example, you can also access the error message using as, like this:

except Exception as e:
    print(e)

Assignment

Take a look at the get_player_record function. It raises an exception for negative player_id's.

Complete the handle_get_player_record() function. It should return the result of get_player_record, but if an IndexError is raised, it will instead return the string: index is too high. Otherwise, if any other exception is raised, handle it and return its inner message.
"""

def handle_get_player_record(player_id):
    try:
        return(get_player_record(player_id))
    except IndexError:
        return('index is too high')
    except Exception as e:
        return(e)

# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]


"""
---------------------------------
Inputs: 0
Expecting: {'name': 'Slayer', 'level': 128}
Actual: {'name': 'Slayer', 'level': 128}
Pass
---------------------------------
Inputs: 1
Expecting: {'name': 'Dorgoth', 'level': 300}
Actual: {'name': 'Dorgoth', 'level': 300}
Pass
---------------------------------
Inputs: 3
Expecting: index is too high
Actual: index is too high
Pass
---------------------------------
Inputs: -1
Expecting: negative ids not allowed
Actual: negative ids not allowed
Pass
---------------------------------
Inputs: 2
Expecting: {'name': 'Saruman', 'level': 4000}
Actual: {'name': 'Saruman', 'level': 4000}
Pass
---------------------------------
Inputs: 10
Expecting: index is too high
Actual: index is too high
Pass
---------------------------------
Inputs: -5
Expecting: negative ids not allowed
Actual: negative ids not allowed
Pass
============= PASS ==============
7 passed, 0 failed
"""