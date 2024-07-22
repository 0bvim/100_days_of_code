import random

'''
Blackjack / 21

The goal of  this game is have the biggest amounting cards withou pass 21
If will got more than 21, you lose. Cards from 2 to 10 have itself value.
Jack, Queen and King count as 10. Ace count 1 or 11 - You decide value,
if come over or not 21 when you choose value

Flowchart of this class
https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
'''

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

def verify_player_score(cards):
	return sum(cards) > 21

def verify_initial_score(user, computer):
	if (has_black_jack(user) and has_black_jack(computer)):
		print ("Draw")
		exit(0)
	elif (has_black_jack(computer)):
		print("You lose!")
		exit(0)
	elif (has_black_jack(user)):
		print("You win!")
		exit(0)

def print_score(user, computer):
	print(f"Your score: {sum(user)}\nComputer score: {sum(computer)}")

def ace_check(cards):
	if cards.count(11):
		return True

def keep_playing(user, computer):
	if verify_player_score(user):
		if ace_check(user):
			user = [1 if x == 11 else x for x in user]
			print(f"You have Ace of Spades!\nThis is your list {user}")

def start_game():
	user_cards = [11, 5, 10]
	comp_cards = []

	# TODO this generate random cards. I'm doing now specific tests
	for _ in range(2):
		# user_cards.append(deal())
		comp_cards.append(deal())
	
	print_score(user_cards, comp_cards)
	verify_initial_score(user_cards, comp_cards)
	keep_playing(user_cards, comp_cards)
	# print(f"user {has_black_jack(user_cards)}\ncomp {has_black_jack(comp_cards)}")
	# print(f"user {sum(user_cards)}\ncomp {sum(comp_cards)}")

def general_game_loop():
	while (play_game("Do you wanna play blackjack? ")):
		start_game()

general_game_loop()
