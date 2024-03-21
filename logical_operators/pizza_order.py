print("Thank you for choosing Python Pizza Deliveries!")
size = input("Choose size of your pizza. S, M or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size.upper() == "L":
    bill = 25
elif size.upper() == "M":
    bill = 20
elif size.upper() == "S":
    bill = 15
if add_pepperoni.upper() == "Y":
    bill += 3
if extra_cheese.upper() == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")
