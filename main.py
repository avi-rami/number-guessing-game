from art import logo
import random

print(logo)

print("Welcome to Guess Quest!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print(f"Pssst, the correct answer is {number}")

# Prompt user to choose difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Set number of attempts based on chosen difficulty
if difficulty == 'easy':
    attempts_left = 10
elif difficulty == 'hard':
    attempts_left = 5
# NTS - add error handling for invalid difficulty input

correct_guess = False

# Main game loop
while attempts_left > 0:
    print(f"You have {attempts_left} attempts remaining to guess the number")

    # Prompt user to make a guess and convert input to integer
    guess = int(input("Make a guess: "))

    if guess < number:
        print("Too low.")
        if attempts_left != 1:
            print("Guess again.")
    elif guess > number:
        print("Too high.")
        if attempts_left != 1:
            print("Guess again.")
    elif guess == number:
        correct_guess = True
        break

    attempts_left -= 1

# Provide feedback based on whether the guess was correct or not
if correct_guess:
    print(f"You got it! The answer was {number}")
else:
    print("You've run out of guesses, you lose.")
