import random

random_color = ["R", "G", "B", "Y", "W", "O"]
random_list = random.sample(random_color, 6)
list_of_colors = random_list[1:5]

print(list_of_colors)

def Game():
    print("Welcome to Mastermind!", "Attempt to guess the 4 digit code...", "You have 10 attempts to guess the code.")
    print("The code is made up of 4 of the following colors: R, G, B, Y, W, O")

guess_Count = 0
guesses = 10
#guess = input("Enter your guess: ")
#guessed_colors = []

incorrect_Position = 0
correct_Position = 0

for i in range(guesses):
    guess_Count += 1
    guess = input("Enter your guess: ").upper().split()

    if guess == list_of_colors:
        print("You win!")
        break
    elif guess == list_of_colors[1]:
        guess = input("Enter your guess: ").upper().split()
        correct_Position += 1
        print(f"Correct Position: {correct_Position}, Incorrect Position: {incorrect_Position}" )
    elif guess == list_of_colors[2]:
        guess = input("Enter your guess: ").upper().split()
        correct_Position += 1
        print(f"Correct Position: {correct_Position}, Incorrect Position: {incorrect_Position}" )
    elif guess == list_of_colors[3]:
        guess = input("Enter your guess: ").upper().split()
        correct_Position += 1
        print(f"Correct Position: {correct_Position}, Incorrect Position: {incorrect_Position}" )
    else:
        print("You have guessed incorrectly! Please try again.")
        print(f"Correct Position: {correct_Position}, Incorrect Position: {incorrect_Position}" )
        guess = input("Enter your guess: ").upper().split()
    incorrect_Position += 1

if guess_Count == guesses:  # Check if the maximum number of attempts is reached
    print("Game over. You have run out of attempts.")

Game()
