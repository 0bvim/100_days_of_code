import platform
import random
import game_data
import os
import art

def clear_console():
    command = 'cls' if platform.system().lower() == 'windows' else 'clear'
    os.system(command)

def clear_print():
	clear_console()
	art.print_logo()

def qa_fun(message):
	answer = input(message).upper()
	return answer

def print_info(person):
	print("Name: ", person['name'] + ', ', end = ' ')
	print("Description: ", person['description'] + ", ", end = ' ')
	print("Country: ", person['country'])

def compare():
	keep_playing = True
	streak = 0 

	while(keep_playing):
		clear_print()
		choice_a = random.choice(game_data.data)
		choice_b = random.choice(game_data.data)

		print_info(choice_a)
		print(f"Current Score: {streak}.")
		art.print_vs()
		print_info(choice_b)
		asw = qa_fun("Who has more followers? Type 'A' or 'B': ")
		if asw == 'A' and choice_a['follower_count'] > choice_b['follower_count']:
			streak += 1
			continue;
		elif asw == 'B' and choice_b['follower_count'] > choice_a['follower_count']:
			streak += 1
			continue;
		else:
			print("You lose. Final Game, bye bye")
			break;

def routine():
	clear_print()
	compare()

routine()
