"""
Bitwise "&" Operator

Bitwise operators are similar to logical operators, but instead of operating on boolean values, they apply the same logic to all the bits in a value by column. For example, say you had the numbers 5 and 7 represented in binary. You could perform a bitwise "and" operation and the result would be 5.

    0101 is 5
    0111 is 7

0101
&
0111
=
0101

A 1 in binary is the same as True, while 0 is False. So really a bitwise operation is just a bunch of logical operations that are completed in tandem by column.

0 & 0 = 0

1 & 1 = 1

1 & 0 = 0

Ampersand & is the bitwise "and" operator in Python. "And" is the name of the bitwise operation, while ampersand & is the symbol for that operation. For example, 5 & 7 = 5, while 5 & 2 = 0.

    0101 is 5
    0010 is 2

0101
&
0010
=
0000

Binary notation

When writing a number in binary, the prefix 0b is used to indicate that what follows is a binary number.

    0b0101 is 5
    0b0111 is 7

Putting It Together

0b0101 & 0b0111
# equals 5

binaryFive = 0b0101
binarySeven = 0b0111
binaryFive & binarySeven
# equals 5

Guild Permissions

Sometimes applications store user permissions as binary values. If I have 4 different permissions a user can have, then I can store that as a 4-digit binary number, and if a certain bit is present, I know the permission is enabled. This can be a lot more efficient than storing entire strings.

Let's pretend we have 4 permissions related to "guilds" in Fantasy Quest ("guild" is just a fancy videogame word for "team"):

    can_create_guild - Leftmost bit (0b1000)
    can_review_guild - Second to leftmost bit (0b0100)
    can_delete_guild - Second to rightmost bit (0b0010)
    can_edit_guild - Rightmost bit (0b0001)

If a user has no permissions, their binary permissions would be 0b0000.

If a user only has the can_create_guild permission, their binary permissions would be 0b1000, but a user with can_review_guild and can_edit_guild permissions would be 0b0101.

To check for, say, the can_review_guild permission, we can perform a bitwise and operation on the user's permissions and the enabled can_review_guild bit (0b0100). If the result is 0b0100 again, we know they have that specific permission!
Assignment

Complete each of the get_XXX_bits functions. Use the bitwise & operation on the user's permission bits and the appropriate guild permission bits, and return the resulting bits.

4 values have been provided, use the appropriate one for each function:

    can_create_guild
    can_review_guild
    can_delete_guild
    can_edit_guild

Note: The get_XXX_bits functions return the bits and the test code compares the result to the original permission value to see if it matches!
"""
#notes: 
# bitwise '&' operator:  
# is used to 
    # build authentication, 
    # squeeze/compress data for optimal storage 
    # and used in network communications
# 0101 is 5 and 0111 is 7
    #   0101 &
    #   0111
    # = 0101
# with bitwise & operator, we go by column
    #   0101        // 5
    #   &          
    #   0111        // 7
    #   =  
    #   0101        // 5

# binary & Operator will always produce the total number of 1s in the output.

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

def get_create_bits(user_permissions):
    return can_create_guild & user_permissions

def get_review_bits(user_permissions):
    return can_review_guild & user_permissions

def get_delete_bits(user_permissions):
    return can_delete_guild & user_permissions

def get_edit_bits(user_permissions):
    return can_edit_guild & user_permissions


"""
---------------------------------
Inputs: 0110
Expecting can_create: False
Expecting can_review: True
Expecting can_delete: True
Expecting can_edit: False
Actual can_create: False
Actual can_review: True
Actual can_delete: True
Actual can_edit: False
Pass
---------------------------------
Inputs: 1111
Expecting can_create: True
Expecting can_review: True
Expecting can_delete: True
Expecting can_edit: True
Actual can_create: True
Actual can_review: True
Actual can_delete: True
Actual can_edit: True
Pass
---------------------------------
Inputs: 0000
Expecting can_create: False
Expecting can_review: False
Expecting can_delete: False
Expecting can_edit: False
Actual can_create: False
Actual can_review: False
Actual can_delete: False
Actual can_edit: False
Pass
---------------------------------
Inputs: 1001
Expecting can_create: True
Expecting can_review: False
Expecting can_delete: False
Expecting can_edit: True
Actual can_create: True
Actual can_review: False
Actual can_delete: False
Actual can_edit: True
Pass
---------------------------------
Inputs: 1000
Expecting can_create: True
Expecting can_review: False
Expecting can_delete: False
Expecting can_edit: False
Actual can_create: True
Actual can_review: False
Actual can_delete: False
Actual can_edit: False
Pass
---------------------------------
Inputs: 0100
Expecting can_create: False
Expecting can_review: True
Expecting can_delete: False
Expecting can_edit: False
Actual can_create: False
Actual can_review: True
Actual can_delete: False
Actual can_edit: False
Pass
---------------------------------
Inputs: 0010
Expecting can_create: False
Expecting can_review: False
Expecting can_delete: True
Expecting can_edit: False
Actual can_create: False
Actual can_review: False
Actual can_delete: True
Actual can_edit: False
Pass
---------------------------------
Inputs: 0001
Expecting can_create: False
Expecting can_review: False
Expecting can_delete: False
Expecting can_edit: True
Actual can_create: False
Actual can_review: False
Actual can_delete: False
Actual can_edit: True
Pass
============= PASS ==============
8 passed, 0 failed
"""
