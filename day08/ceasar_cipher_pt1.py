alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    end_text = ""
    for letter in text:
        if direction == "encode":
            end_text += chr((ord(letter) - 97 + shift) % 26 + 97)
        elif direction == "decode":
            end_text += chr((ord(letter) - 97 - shift) % 26 + 97)
        else:
            exit("Invalid input")
    print(f"Content is {end_text}")

caesar(text=text, direction=direction, shift=shift)
