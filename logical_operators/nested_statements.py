print("Welcome to the rollecoaster")
height = int(input("Type your height in centimeters: "))

bill = 0
if height >= 120:
    print("Nice, you can ride dude!")
    age = int(input("Tell me your age and I'll tell you the price of ticket: "))
    if age > 18:
        bill = 12
        print(f"{bill} is the price of ticket")
    elif age >= 12 and age <= 18:
        bill = 7
        print(f"{bill} is the price of ticket")
    else:
        bill = 5
        print(f"{bill} is the price of ticket")

    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you can't ride")
