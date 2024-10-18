"""
Modulo operator in Python
The modulo operator can be used to find a remainder:

For example, 7 modulo 2 would be 1, because 2 can be multiplied evenly into 7 at most 3 times:

2 * 3 = 6

Then there is 1 remaining to get from 6 to 7.

7 - 6 = 1

The modulo operator is the percent sign: %. It's important to recognize modulo is not a percentage though! That's just the symbol we're using.

remainder = 8 % 3
# remainder = 2

An odd number is a number that when divided by 2, the remainder is not 0.
Assignment

Inside the loop in the get_odd_numbers function, use the modulo operator to check if each number, i, is odd. If a number is odd, append it to the odd_numbers list. The function already returns the odd_numbers list for you. num is an integer.
"""

def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        if i % 2 != 0:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers


"""
---------------------------------
Inputs: 10
Expecting: [1, 3, 5, 7, 9]
Actual: [1, 3, 5, 7, 9]
Pass
---------------------------------
Inputs: 20
Expecting: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Actual: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Pass
---------------------------------
Inputs: 0
Expecting: []
Actual: []
Pass
---------------------------------
Inputs: 1
Expecting: []
Actual: []
Pass
---------------------------------
Inputs: 2
Expecting: [1]
Actual: [1]
Pass
---------------------------------
Inputs: 300
Expecting: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 
149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207, 209, 211, 213, 215, 217, 219, 221, 223, 225, 227, 229, 231, 233, 235, 237, 239, 241, 243, 245, 247, 249, 251, 253, 255, 257, 259, 261, 263, 265, 267, 269, 271, 273, 275, 277, 279, 281, 283, 285, 287, 289, 291, 293, 295, 297, 299]
Actual: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207, 209, 211, 213, 215, 217, 219, 221, 223, 225, 227, 229, 231, 233, 235, 237, 239, 241, 243, 245, 247, 249, 251, 253, 255, 257, 259, 261, 263, 265, 267, 269, 271, 273, 275, 277, 279, 
281, 283, 285, 287, 289, 291, 293, 295, 297, 299]
Pass
============= PASS ==============
6 passed, 0 failed
"""