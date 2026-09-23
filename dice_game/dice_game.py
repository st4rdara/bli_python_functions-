"""
Dice Game

A simple command-line dice game that allows the player
to roll a six-sided die and play multiple rounds.
"""

import random


def roll_die():
    """Generate and return a random number from 1 to 6."""
    return random.randint(1, 6)


def display_result(roll):
    """Display the result of the player's roll."""
    print(f"You rolled: {roll}")


def play_again():
    """Ask the player whether they want to roll again."""
    while True:
        response = input("Would you like to roll again? (y/n): ")

        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Please enter y or n.")


def main():
    """Run the dice game."""
    print("Welcome to the Dice Game!")

    while True:
        input("Press Enter to roll the die...")

        roll = roll_die()
        display_result(roll)

        if not play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
