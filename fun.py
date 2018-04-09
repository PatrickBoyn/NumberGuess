import random
import math

x = math.floor(random.random() * 10 + 1)
z = math.floor(random.random() * 20 + 1)
counter = 0

beginning = input("Please select a mode, (e)asy or (h)ard\n")

if beginning == "e":
    while True:
        y = int(input("Guess a number between 1 and 10: "))
        if x == y:
            print("Good job, the number was {}".format(x))
            break
        else:
            print("Please try again.")
            counter += 1
            if counter == 5:
                print("Game over.")
                break
elif beginning == "h":
    while True:
        y = int(input("Guess a number between 1 and 20: "))
        if z == y:
            print("Good job, the number was {}".format(z))
            break
        else:
            print("Please try again.")
            counter += 1
            if counter == 3:
                print("Game over.")
                break
            print(z)
