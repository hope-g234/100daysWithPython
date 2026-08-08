import random


hangman_ascii = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
# randomly choose a word
print("Welcom to Hangman,Start guessing name of animal")

lives=6
choosen_word=random.choice(word_list)
#print(choosen_word)

placeholder =""

for position in range(len(choosen_word)):
    placeholder+="_"

print(placeholder)

correct_letter =[]

game_over = False

while not game_over:

    display=""
    print(f"******************************************{lives}/6 Lives Left**********************")
    guess= input("Guess a letter:").lower()
    # print(guess)
    if guess in correct_letter:
        print(f"You've already guessed {guess}")


    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display +="_"

    print(display)

    if guess not in choosen_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word.You lose a life!")
        if lives==0:
            game_over = True
            print("************You Lose!**************")




    if "_" not in display:
        game_over = True
        print("You guessed the word!")

    print(hangman_ascii[lives])