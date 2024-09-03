import random
import pandas
# working with list comprehension

numbers = [1, 2, 3]
new_nembers = [number + 1 for number in numbers]
print(new_nembers)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [number * 2 for number in range(1,5)]
print(range_list)

names = ["Lila", "Nivi", "Steh", "Maria", "Pereira", "To", "Biba"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

# working with dict comprehension

students_scores = {student:random.randint(1,100) for student in names}
print (students_scores)

passed_students = {key:value for (key, value) in students_scores.items() if value > 50}
print(passed_students)

# loop in dict
for (key, value) in students_scores.items():
	print(value)

students_data_frame = pandas.DataFrame(students_scores)
print(students_data_frame)
