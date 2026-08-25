import random
from art import logo

print(logo)

print("Wlcome to the game Blackjack!")

def deal_cards():
    """ Returns a random card from the  deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw😑"
    elif computer_score == 0:
        return "lose,opponent has Blackjack😬"
    elif user_score == 0:
        return"Win with Blackjack😎"
    elif user_score > 21 :
        return " You went over.You lose😟"
    elif computer_score > 21:
        return"Opponent went over. You win😃"
    elif user_score > computer_score:
        return"You win😀"
    else:
        return"You lose🙁"

def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        new_card = deal_cards()
        user_cards.append(new_card)
        computer_cards.append(new_card)

    while  not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards:{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_continue = input("Type 'y' to get another card or 'n' to pass: ")
            if user_should_continue == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True


    while computer_score !=0 and computer_score <= 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand:{user_cards}, final score: {user_score}")
    print(f"Computer's final hand:{computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack ? Type 'y' or 'n' : ") == "y":
    print("\n" *20)
    play_game()