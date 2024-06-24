students_heights = input().split()

total_heigth = 0
nbr_students = 0
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
    total_heigth += int(students_heights[n])
    nbr_students += 1
print(f"total height = {total_heigth}")
print(f"number of students = {nbr_students}")
print(f"average height = {round(total_heigth / nbr_students)}")
