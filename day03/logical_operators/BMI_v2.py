print("Welcome to Body Mass Index calculator 2.0")

height = float(input("Type your height in cm: "))
weight = input("Type your weight in kg: ")
bmi = int(weight) / float((height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You're underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You're slightly underweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You're obese.")
else:
    print(f"Your BMI is {bmi}. You're clinically obese.")
