print("Welcome to the tip calculator.\n")
bill = input("What was the total bill? ")
tip = input("What the percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

total_bill = float(bill) + ((int(tip) / 100) * float(bill))
final_value = round(total_bill / int(people), 2)
print(f"Each person should pay {final_value}")
