from secrets import choice
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps_list = [rock, paper, scissors ]

print("Welcom to rock paper scissors")
choice = ["rock", "paper", "scissors" ]
user_choice = int(input("Please enter your choice: 0 for rock , 1 for paper and 2 for scissors\n "))
print(rps_list[user_choice])
computer_choice = random.randint(0,2)
print(f"Computer choice : {computer_choice}")
print(rps_list[computer_choice])

if user_choice >=3 or user_choice < 0:
    print("you typed wrong number")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")

elif computer_choice ==  user_choice:
    print("it's a tie!")
elif computer_choice == 0 and user_choice == 2 :
    print("You lose!")

elif computer_choice > user_choice:
    print("you lost the Game!")
elif computer_choice < user_choice:
    print("you won!")

