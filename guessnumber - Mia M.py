import random
import time

number = random.randint(1,100)

guess = 0

counter = 0

while True:
    counter += 1
    print("Guess my number between 1 and 100!")
    guess = int(input())

    if guess == number:
        print("You got it! Nice job!")
        print("You took " + str(counter) + " guesses.")
        break

    elif guess > number:
        print("Too high! Try again.")

    elif guess < number:
        print("too low! Try again.")
