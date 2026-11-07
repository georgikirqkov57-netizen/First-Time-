
# Week 4 - Modules
# Activity: Guess the Number

# Import the random module
import random


# Function to play the guessing game
def play_guess_the_number():

    # Ask the user for the minimum and maximum values
    print("Please enter the minimum value:")
    minimum = int(input())

    print("Please enter the maximum value:")
    maximum = int(input())

    # Generate a random number
    secret_number = random.randint(minimum, maximum)

    print(f"I am thinking of a number between {minimum} and {maximum}. Can you guess what it is?")

    # Keep asking until the user guesses correctly
    guess = int(input())

    while guess != secret_number:

        if guess < secret_number:
            print("Your guess is too low.")

        else:
            print("Your guess is too high.")

        print("Try again:")
        guess = int(input())

    # Display the winning message
    print("Congratulations! You guessed my number!")


# Start the game
play_guess_the_number()
