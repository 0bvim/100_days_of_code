alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text=text, shift=shift):
    shifted = ""
    for letter in text:
        shifted += chr((ord(letter) - 97 + shift) % 26 + 97)
    print(f"Encryped content is {shifted}")

def decrypt(text=text, shift=shift):
    shifted = ""
    for letter in text:
        shifted += chr((ord(letter) - 97 - shift) % 26 + 97)
    print(f"decrypted content is {shifted}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid input")

