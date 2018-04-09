import random
import math

# PEP-8 Says that variables outside methods or classes should be
# in all caps. 
EASY = math.floor(random.random() * 10 + 1)
HARD = math.floor(random.random() * 20 + 1)
COUNTER = 0

BEGINNING = input("Please select a mode, (e)asy or (h)ard\n")

# This is easy mode. If the user picks e, then this is run. 
if BEGINNING == "e":
    while True:
        print("You have 5 guesses to guess the right number. ")
        GUESS = int(input("Guess a number between 1 and 10: "))
        # Winning conditions.
        if GUESS == EASY:
            print("Good job, the number was {}".format(EASY))
            break
        else:
            # If the user guesses wrong.
            print("Please try again.")
            COUNTER += 1
            # For testing purposes only.
            print("The guess is {0} and the counter is at {1}".format(EASY, COUNTER))
            # Game over and loose conditions.
            if COUNTER == 5:
                print("Game over.")
                break
# Same logic as above. When I learn more about classes and instances.
# I will turn this into a Game class and make an easy and hard instance. 
elif BEGINNING == "h":
    while True:
        print("You have 3 guesses to guess the number. ")
        GUESS = int(input("Guess a number between 1 and 20: "))
        if GUESS == HARD:
            print("Good job, the number was {}".format(HARD))
            break
        else:
            print("Please try again.")
            # For testing purposes only. 
            print("The guess is {0} and the counter is at {1}".format(EASY, COUNTER))
            COUNTER += 1
            if COUNTER == 3:
                print("Game over.")
                break
