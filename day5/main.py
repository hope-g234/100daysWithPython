import random
from random import shuffle

print("Welcome to PyPassword Generation")
# List of numbers (0 to 9)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List of common punctuation symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# List of letters (lowercase a to z)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

number_of_letters = int(input("How many letter would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like in your password?\n"))
number_of_numbers = int(input("How many numbers would you like in your password?\n"))

password = ''
for letter in range(number_of_letters):
    password += random.choice(letters)
for sym in range(number_of_symbols):
    password += random.choice(symbols)
for number in range(number_of_numbers):
    password += str(random.choice(numbers))

first_letter = password[0].capitalize()
remaining_char = password[1:]
password_list = list(remaining_char)
random.shuffle(password_list)
final_password = first_letter + "".join(password_list)
print(final_password)

