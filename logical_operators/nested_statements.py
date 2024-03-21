print("Welcome to the rollecoaster")
height = int(input("Type your height in centimeters: "))

if height >= 120:
    print("Nice, you can ride dude!")
    age = int(input("Tell me your age and I'll tell you the price of ticket: "))
    if age > 18:
        print("$12 is the price of ticket")
    elif age >= 12 and age <= 18:
        print("$7 is the price of ticket")
    else:
        print("$5 is the price of ticket")
else:
    print("Sorry, you can't ride")
