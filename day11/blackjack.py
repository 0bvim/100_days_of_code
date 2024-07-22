import random
import os
import platform

'''
Blackjack / 21

The goal of  this game is have the biggest amounting cards withou pass 21
If will got more than 21, you lose. Cards from 2 to 10 have itself value.
Jack, Queen and King count as 10. Ace count 1 or 11 - You decide value,
if come over or not 21 when you choose value

Flowchart of this class
https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
'''

def clear_console():
    command = 'cls' if platform.system().lower() == 'windows' else 'clear'
    os.system(command)

def play_game(message):
	answer = input(message).lower()

	if answer == "y" or answer == "yes":
		return True
	elif answer == "n" or answer == "no":
		return False

def deal():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)

def has_black_jack(cards):
	points = sum(cards)
	if (points == 21):
		return True
	return False

def verify_players_score(user, computer):
	return sum(user) > 21 or sum(computer) > 21

def verify_player_score(cards):
	return sum(cards) > 21

def verify_score(user, computer):
	if (has_black_jack(user) and has_black_jack(computer)):
		print ("Draw")
		print_score(user, computer)
		exit(0)
	elif (has_black_jack(computer) or verify_player_score(user)):
		print("You lose!")
		print_score(user, computer)
		exit(0)
	elif (has_black_jack(user) or verify_player_score(computer)):
		print("You win!")
		print_score(user, computer)
		exit(0)
	else:
		return False

def print_score(user, computer):
	print(f"Your score: {sum(user)}\nComputer score: {sum(computer)}")

def ace_check(cards):
	if cards.count(11):
		return True
	return False

def players_ace_cards(user, computer):
	if verify_players_score(user, computer):
		if ace_check(user):
			user = [1 if x == 11 else x for x in user]
			if ace_check(user):
				print("You lose!")
				exit(0)
		if ace_check(computer):
			computer = [1 if x == 11 else x for x in computer]
			if ace_check(computer):
				print("You win!")
				exit(0)

def keep_playing(user, computer):
	while (play_game("Do you want to get another card? ")):
		if verify_score(user, computer) == False:
			players_ace_cards(user, computer)
			verify_score(user, computer)
			user.append(deal())
			computer.append(deal())
			verify_score(user, computer)
			continue;
		user.append(deal())
		computer.append(deal())
		verify_score(user, computer)
		print_score(user, computer)
	computer.append(deal())
	verify_score(user, computer)

def start_game():
	user_cards = []
	comp_cards = []

	for _ in range(2):
		user_cards.append(deal())
		comp_cards.append(deal())
	
	print_score(user_cards, comp_cards)
	verify_score(user_cards, comp_cards)
	keep_playing(user_cards, comp_cards)

def general_game_loop():
	while (play_game("Do you wanna play blackjack? ")):
		start_game()
	print("Bye Bye!")

general_game_loop()
