"""
Errors and exceptions in Python

You've probably encountered some errors in your code from time to time if you've gotten this far in the course. In Python, there are two main kinds of distinguishable errors.

    syntax errors
    exceptions

Syntax errors

You probably know what these are by now. A syntax error is just the Python interpreter telling you that your code isn't adhering to proper Python syntax.

this is not valid code, so it will error

If I try to run that sentence as if it were valid code I'll get a syntax error:

this is not valid code, so it will error
      ^
SyntaxError: invalid syntax

Exceptions

Even if your code has the right syntax, however, it may still cause an error when an attempt is made to execute it. Errors detected during execution are called "exceptions" and can be handled gracefully by your code. You can even raise your own exceptions when bad things happen in your code.

Python uses a try-except pattern for handling errors.

try:
  10 / 0
except Exception:
  print("can't divide by zero")

The try block is executed until an exception is raised or it completes, whichever happens first. In this case, an exception is raised because division by zero is impossible. The except block is only executed if an exception is raised in the try block.

If we want to access the data from the exception, we use the following syntax:

try:
  10 / 0
except Exception as e:
  print(e)

# prints "division by zero"

Wrapping potential errors in try/except blocks allows the program to handle the exception gracefully without crashing.
Assignment

One of the calls to get_player_record is throwing a player id not found exception. Change the code in the main function to safely make all four calls within one try-except block. If an exception is raised, print the exception instead.
"""

def main():
    try:
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
    except Exception as e:
        print(e)

# Don't edit below this line


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")


main()
