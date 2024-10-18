"""
If Statements

It's often useful to only execute code if a certain condition is met:

if CONDITION:
	# do some stuff here

# code after the if block will run regardless

For example, in this code:

if bob_score > bill_score:
	print("Bob Wins!")

print("Game Complete")

if bob_score is greater than bill_score, then this will be printed:

Bob Wins!
Game Complete

Otherwise, this will be printed:

Game Complete

Assignment

Complete the print_status function.

    If player_health is 0, print the text dead to the console.
    Afterwards, whether or not the player is dead, print the text status check complete to the console.

Tip

Indentation matters! Indentation is what tells Python whether the body of a function or the if statement has ended. Also, don't forget the colon after your if statement : it is a required part of the syntax!
"""

def print_status(player_health):
    if player_health == 0:
        print("dead")
    print(f"player health is currently: {player_health}, status check complete")


# Don't edit below this line


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(3)


main()

