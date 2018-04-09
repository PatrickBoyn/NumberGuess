import random
import math

EASY = math.floor(random.random() * 10 + 1)
HARD = math.floor(random.random() * 20 + 1)
COUNTER = 1

BEGINNING = input("Please select a mode, (e)asy or (h)ard\n")

if BEGINNING == "e":
    while True:
        GUESS = int(input("Guess a number between 1 and 10: "))
        if GUESS == EASY:
            print("Good job, the number was {}".format(EASY))
            break
        else:
            print("Please try again.")
            COUNTER += 1
            # For testing purposes only.
            print("The guess is {0} and the counter is at {1}".format(EASY, COUNTER))
            if COUNTER == 5:
                print("Game over.")
                break
elif BEGINNING == "h":
    while True:
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
