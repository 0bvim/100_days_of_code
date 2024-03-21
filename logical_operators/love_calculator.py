print("The love calculator is calculating your score...")
name1 = input("What's your name? ")
name2 = input("What's their name? ")
concat_names = name1 + name2
concat_names = concat_names.lower()
t = concat_names.count("t")
r = concat_names.count("r")
u = concat_names.count("u")
e = concat_names.count("e")
first_digits = t + r + u + e

l = concat_names.count("l")
o = concat_names.count("o")
v = concat_names.count("v")
e = concat_names.count("e")
second_digits = l + o + v + e

score = int(str(first_digits) + str(second_digits))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
