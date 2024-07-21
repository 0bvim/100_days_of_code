import random

'''
Blackjack / 21

The goal of  this game is have the biggest amounting cards withou pass 21
If will got more than 21, you lose.

Cards from 2 to 10 have itself value
Jack, Queen and King count as 10. 
Ace count 1 or 11 - You decide value,
if come over or not 21 when you choose value
https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

'''

def deal():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)

user_cards = []
comp_cards = []

for _ in range(2):
	user_cards.append(deal())
	comp_cards.append(deal())

sum_user = sum(user_cards)
sum_comp = sum(comp_cards)

print(f"user {sum_user}\ncomp {sum_comp}")
