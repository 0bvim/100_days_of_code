# to modify global variables we should use 'global' keyword before variable name
# convention to Global constants is use all letters CAPITAL in var name

from logo import logo
import logo
import random
import platform
import os

def clear_console():
    command = 'cls' if platform.system().lower() == 'windows' else 'clear'
    os.system(command)

def clear_print():
	clear_console()
	print(logo)

def qa_fun(message):
	answer = input(message).lower()
	return answer in ["y", "yes"]

def choose_level():
	return input("Choose a difficult. Type 'easy' or 'hard' ").lower()

def hint(answer, number):
	if answer > number:
		print("Too high")
	elif answer < number:
		print("Too low")

guess = False

def game_start():
	global guess

	difficult = choose_level()
	attempts = 100 if difficult == "hard" else 10
	number = random.randint(1, 100)
	user_history = []
	clear_print()

	while not guess:
		print(f"\nAttemps: {attempts}")
		if not attempts > 0:
			clear_console()
			print("You lose =/")
			break;
		answer = int(input("Guess a number: "))
		
		if answer == number:
			guess = True
			logo.big_seq()
		elif answer not in user_history:
			hint(answer, number)
			user_history.append(answer)
			print ("Guessed: ", end =' ')
			[print(item, end=' ') for item in user_history]
		else:
			print ("You already guessed this number! Try again")
		attempts -= 1

	print("Bye bye")

game_start()
