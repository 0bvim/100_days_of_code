import string
import random

letters = list(string.ascii_letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']

print("Welcome to the password generator")
letters_nb = int(input("How many letter would you like in your password? "))
symbols_nb = int(input("How many symbols would you like in your password? "))
numbers_nb = int(input("How many numbers would you like in your password? "))

password_list = []

for char in range(1, letters_nb + 1):
    password_list.append(random.choice(letters))

for sym in range(1, symbols_nb + 1):
    password_list.append(random.choice(symbols))

for num in range(1, numbers_nb + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

final_str = ""
for char in password_list:
    final_str += char
print(f"Your password is: {final_str}")

