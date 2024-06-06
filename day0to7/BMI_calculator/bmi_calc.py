print("Welcome to Body Mass Index calculator\n")

weight = input("Type your weight: ")
height = float(input("Type your height: "))
bmi = int(weight) / float((height ** 2))

print (f"Your BMI is {bmi}")

# F strings allow you print variables just using curly braces envolving the variable name
