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


def print_blanks(blanks):
    for i in range(blanks):
        print("_", end="")
    print("")


word = random.choice(words)

print_blanks(len(word))
