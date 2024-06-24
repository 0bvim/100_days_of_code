scores = input().split()

max_number = -1
for n in range(0, len(scores)):
    scores[n] = int(scores[n])
    if scores[n] > max_number:
        max_number = scores[n]
print(f"The highest score in the class: {max_number}")
