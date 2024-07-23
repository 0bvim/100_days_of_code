from logo import logo
import platform
import random
import os

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
	return answer in ["y", "yes"]

def deal():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)

def has_blackjack(cards):
	return sum(cards) == 21

def adjust_for_ace(cards):
	while sum(cards) > 21 and 11 in cards:
		cards[cards.index(11)] = 1
	return cards

def calculate_score(cards):
	return sum(adjust_for_ace(cards))

def game_result(user, computer):
	if has_blackjack(user) and has_blackjack(computer):
		return "Draw!"
	elif has_blackjack(computer):
		return "You lose! Computer has Blackjack."
	elif has_blackjack(user):
		return "You win! You have Blackjack."
	elif calculate_score(user) > 21:
		return "You lose! Your score went over 21."
	elif calculate_score(computer) > 21:
		return "You win! Computer's score went over 21."
	elif calculate_score(user) == calculate_score(computer):
		return "Draw!"
	elif calculate_score(user) > calculate_score(computer):
		return "You win!"
	else:
		return "You lose!"

def print_score(user, computer):
	print(f"Your cards: {user} - Your score: {sum(user)}\nComputer score: {sum(computer)}")

def start_game():
	user_cards = [deal(), deal()]
	comp_cards = [deal(), deal()]
	
	print_score(user_cards, comp_cards)
	if not (has_blackjack(user_cards) or has_blackjack(comp_cards)):
		while play_game("Do you want to get another card? "):
			user_cards.append(deal())
			print_score(user_cards, comp_cards)
			if calculate_score(user_cards) > 21 or has_blackjack(user_cards):
				break
	
	while calculate_score(comp_cards) < 17:
		comp_cards.append(deal())

	print(game_result(user_cards, comp_cards))

def general_game_loop():
	clear_console()
	print(logo)
	while (play_game("Do you wanna play blackjack? ")):
		clear_console()
		print(logo)
		start_game()
	print("Bye Bye!")

# ensures that the general game loop function is executed onlywhen the scrpt is run directly
# not when it's imported as a module in another script

if __name__ == "__main__":
    general_game_loop()
