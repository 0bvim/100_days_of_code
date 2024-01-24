print("Welcome to Body Mass Index calculator\n")

weight = input("Type your weight: ")
height = float(input("Type your height: "))
bmi = int(weight) / float((height ** 2))

print ("Your BMI is " + str(bmi))
