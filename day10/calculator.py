def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

print("choose one of the following operations")
for key in operations:
    print(key)

operation = input("Which opertion you want?: ")

calculation_function = operations[operation]

print(f"{num1} {operation} {num2} = {calculation_function(num1, num2)}")
