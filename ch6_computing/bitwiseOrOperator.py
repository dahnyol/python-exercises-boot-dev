"""
Bitwise "|" Operator

As you may have guessed, the bitwise "or" operator is similar to the bitwise "and" operator in that it works on binary rather than boolean values. However, the bitwise "or" operator "or"s the bits together. Here's an example:

    0101 is 5
    0111 is 7

0101
|
0111
=
0111

A 1 in binary is the same as True, while 0 is False. So a bitwise operation is just a bunch of logical operations that are completed in tandem. When two binary numbers are "or"ed together, the result has a 1 in any place where either of the input numbers has a 1 in that place.

| is the bitwise "or" operator in Python. 5 | 7 = 7 and 5 | 2 = 7 as well!

    0101 is 5
    0010 is 2

0101
|
0010
=
0111

Guild Permissions

A "guild" is a team of 2-4 players. Here are the guild-specific permissions:

    can_invite - Leftmost bit (0b1000)
    can_kick - Second to leftmost bit (0b0100)
    can_enter_dungeon - Second to rightmost bit (0b0010)
    can_surrender - Rightmost bit (0b0001)

When players are in a guild together, they gain all the permissions of all the other members of the guild!

For example, if:

    Jack has the can_invite permission: 0b1000
    Jill has the can_kick permission: 0b0100

Then, when they are partied together, they should both have the can_invite and can_kick permissions: 0b1100.
Assignment

Complete the calculate_guild_perms function. It should return a binary number that represents the permissions of all the members of the guild (Glorfindel, Galadriel, Elendil and Elrond).

Use a series of bitwise "or" operations to calculate the superset of all the member's permissions.
"""

# can_invite = (0b1000)
# can_kick = (0b0100)
# can_enter_dungeon = (0b0010)
# can_surrender = (0b0001)

# combine the permissions using bitwise OR | to merge their individual permissions.

def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    combined_perms = glorfindel | galadriel |elendil | elrond
    return combined_perms


"""
---------------------------------
Inputs: 1, 2, 1, 11
Expecting: 11
Actual: 11
Pass
---------------------------------
Inputs: 0, 0, 0, 11
Expecting: 11
Actual: 11
Pass
---------------------------------
Inputs: 9, 2, 13, 11
Expecting: 15
Actual: 15
Pass
============= PASS ==============
3 passed, 0 failed
"""