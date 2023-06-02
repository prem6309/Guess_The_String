from random import randint
import random
from random import randrange

random_color = ["R", "G", "B", "Y", "W", "O"]
random_list = random.sample(random_color, 6)

print(random_list[1:5])

def Game():
    print("Welcome to Mastermind!", "Attempt to guess the 4 digit code...", "You have 10 attempts to guess the code.")
    print("The code is made up of 4 of the following colors: R, G, B, Y, W, O")

guess = input("Enter your guess: ")

incorrect_position = 0
correct_position = 0

while guess != random_list:
    if guess == 10:
        print("You have run out of guesses! The code was: ", random_list[1:5])
    elif guess == random_list[1:5]:
        print("You have guessed the code! The code was: ", random_list[1:5])
    else:
        print("You have guessed incorrectly! Please try again.")
        guess = input("Enter your guess: ")

while guess != incorrect_position:
    if incorrect_position == random_list[1:5]:
        incorrect_position += 1
    else:
        correct_position += 1

Game()