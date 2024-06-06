target = int(input("Type a number between 0 and 1000\n"))

total = 0
for number in range(0, target + 1):
    if number % 2 == 0:
        total += number
print(total)
