import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = (
    "thalia", "estephany", "vinicius", "amor", "familia", "papai", "mamae", "saudade",
    "alice", "bob", "charlie", "david", "eve", "frank", "grace", "hannah", "ivy", "jack",
    "kathy", "leo", "mona", "nate", "olivia", "paul", "quincy", "rachel", "steve", "tina",
    "uma", "victor", "wendy", "xander", "yara", "zach", "aiden", "bella", "connor", "diana",
    "ethan", "fiona", "george", "hazel", "ian", "julia", "kevin", "lily", "mason", "nina",
    "oscar", "piper", "quinn", "riley", "sophia", "tyler", "ursula", "violet", "wyatt", "xenia"
)

word = random.choice(words)

display = []
lives = 6

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

    if guess not in word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!!!")

    print(stages[lives])
