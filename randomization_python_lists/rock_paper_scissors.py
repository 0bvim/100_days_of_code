import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

user_choice = int(input("0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice > 2 or user_choice < 0:
    exit(print("Invalid input, you lose!", file=sys.stderr))

print(images[user_choice])

computer_choice = random.randint(0, 2)
print("computer choose:")
print(images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You Win!!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!!")
elif computer_choice > user_choice:
    print("You Lose!!")
elif user_choice > computer_choice:
    print("You Win!!")
elif user_choice == computer_choice:
    print("It's a draw!!!")

