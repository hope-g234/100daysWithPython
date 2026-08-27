import random
from art import  logo

print(logo)

Easy_level_turns = 10
Hard_level_turns = 5

def check_guess(user_guess, actual_answer, turns):
    """check answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("You guessed too high")
        return turns-1
    elif user_guess < actual_answer:
        print("You guessed too low")
        return turns-1
    else:
        print(f"You guessed correctly😃! the answer was {actual_answer}")

def set_difficulty():
    level = input("choose a difficulty😎.Type 'easy' or 'hard': ")
    if level == "easy":
        return Easy_level_turns
    else:
        return Hard_level_turns


def game():

    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100 ")

    computer_choice = random.randint(1,101)
    # print(computer_choice)
    #choose difficulty
    turns = set_difficulty()


    guess = 0
    while guess != computer_choice:
        print(f"You have {turns} attempts remaining to guess the number.")
        #let the user guess a number
        guess = int(input("Make a guess:"))

        turns = check_guess(guess, computer_choice ,turns)

        if turns == 0:
           print("You've run out of guesses! You lose😣")
           return
        elif guess != computer_choice:
            print(f"Guess again")
game()