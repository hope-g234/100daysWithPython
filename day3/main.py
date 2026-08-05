print(r'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcom to Treasure Island! and your mission is to find the treasure.")
choice1 = input('you\'re at a crossroad , where do you want to go? type "left" or "right" \n')

if choice1 == "left":
    Choice2 = input('you\'ve come to a lake.There is an island in the middle of the lake.Type'
          ' "wait" to wait for a boat .'
                    'or "swim" to go to island \n').lower()
    if Choice2 == "wait":
        choice3 = input("you arrive at the island unharmed."
                        "There is house with 3 doors,one red,"
                        "one yellow and one blue."
                        "which color do you choose?\n").lower()
        if choice3 == "red":
            print("its a fire room .Game over!")
        elif choice3 == "yellow":
            print("You found the treasure.You win ! Congratulations!")
        elif choice3 == "blue":
            print(" you entered a room of beasts .Game over!")
        else:
            print(" you choosed the door don't exist. Game over!")
    else:
        print("you got attacked by an allegator ! Game over")
else:
    print("Game over! You fell into a hole")


