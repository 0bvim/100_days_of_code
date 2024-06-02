import random

words = (
    "thalia",
    "estephany",
    "vinicius",
    "amor",
    "familia",
    "papai",
    "mamae",
    "saudade",
)

word = random.choice(words)

display = []

for _ in range(len(word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!!!")
