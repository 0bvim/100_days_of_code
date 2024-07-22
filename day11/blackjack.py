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

def verify_initial_score(user, computer):
	if (has_black_jack(user_cards) and has_black_jack(comp_cards)):
		print ("Draw")
		exit(0)
	elif (has_black_jack(comp_cards)):
		print("You lose!")
		exit(0)
	elif (has_black_jack(user_cards)):
		print("You win!")
		exit(0)

def print_score(user, computer):
	print(f"Your score: {sum(user)}\nComputer score: {sum(computer)}")

while (play_game("Do you wanna play blackjack? ")):

	user_cards = []
	comp_cards = []

	for _ in range(2):
		user_cards.append(deal())
		comp_cards.append(deal())
	
	print_score(user_cards, comp_cards)
	verify_initial_score(user_cards, comp_cards)

	# print(f"user {has_black_jack(user_cards)}\ncomp {has_black_jack(comp_cards)}")
	# print(f"user {sum(user_cards)}\ncomp {sum(comp_cards)}")
