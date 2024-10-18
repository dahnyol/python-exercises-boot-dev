"""
Loops Practice

As a reminder, a "for loop" in Python is written like this:

for i in range(0, 10):
    print(i)

In English, the code says:

    Start with i equals 0. (i in range(0)
    If i is greater than or equal to 10 (range(0, 10)), exit the loop.
    Print i to the console. (print(i))
    Add 1 to i. (range defaults to incrementing by 1)
    Go back to step 2

The result is that the numbers 0-9 are logged to the console in order.
Whitespace matters in Python!

The body of a for-loop must be indented; otherwise, you'll get a syntax error.
Assignment

In the print_numbers_from_five_to function, the for-loop starts at 0. It should start at 5. Only change the start.
"""

def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)


# Don't edit below this line


def test(end):
    print(f"Using input end: {end}")
    print(f"Printing numbers from 5 to {end - 1}:")
    print_numbers_from_five_to(end)
    print("=====================================")


def main():
    test(16)
    test(6)
    test(11)


main()
