"""
Damage Meter

You've been working with some interns to build a damage meter for Fantasy Quest. They've added some calls to the main function that contain invalid syntax.
Assignment

Fix the intern's syntax error. The calculate_dps function takes two inputs but due to the syntax error is taking in 4. Use the proper delimiter so that the numbers are still easy to parse visually.

The two input numbers should be:

    damage: 8 million, time: 45
    damage: 10 million, time: 49
"""

def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)


# Don't edit below this line

def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps:.2f}")
    print("=====================================")

main()
