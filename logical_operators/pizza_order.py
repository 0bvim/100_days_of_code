print("Thank you for choosing Python Pizza Deliveries!")
size = input("Choose size of your pizza. S, M or L? ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

bill = 0
if size == "L":
    bill = 25
elif size == "M":
    bill = 20
elif size == "S":
    bill = 15
if add_pepperoni == "Y" and size == "S":
    bill += 2
else:
    bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")
