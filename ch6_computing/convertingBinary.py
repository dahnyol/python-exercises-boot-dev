"""
Converting Binary

Fantasy Quest needs to migrate old data. Some of their legacy systems stored data as three binary strings which need to be converted to integers.
Assignment

Python has built-in functionality to parse strings of 1's and 0's as binary numbers.

Complete the binary_string_to_int function. It takes three binary strings as input and returns each of them in the same order as integers. Each integer is the numerical value of the string when interpreted as binary.

For example:

data_a, data_b, data_c = binary_string_to_int("100", "101", "110")
print(data_a)
# 4
print(data_b)
# 5
print(data_c)
# 6

Tip

The built-in int function can convert a binary string to an integer. It takes a second argument that specifies the base of the number (binary is base 2). For example:

# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)
"""

def binary_string_to_int(num_servers, num_players, num_admins):
    int_servers = int(num_servers, 2)
    int_players = int(num_players, 2)
    int_admins = int(num_admins, 2)
    return int_servers, int_players, int_admins


"""
---------------------------------
Inputs: 1, 10, 1010
Expecting: (1, 2, 10)
Actual: (1, 2, 10)
Pass
---------------------------------
Inputs: 101, 11, 10100
Expecting: (5, 3, 20)
Actual: (5, 3, 20)
Pass
---------------------------------
Inputs: 111, 1011, 11010
Expecting: (7, 11, 26)
Actual: (7, 11, 26)
Pass
---------------------------------
Inputs: 0, 0, 0
Expecting: (0, 0, 0)
Actual: (0, 0, 0)
Pass
---------------------------------
Inputs: 1111, 1111, 1111
Expecting: (15, 15, 15)
Actual: (15, 15, 15)
Pass
---------------------------------
Inputs: 101010, 110011, 101010
Expecting: (42, 51, 42)
Actual: (42, 51, 42)
Pass
============= PASS ==============
6 passed, 0 failed
"""