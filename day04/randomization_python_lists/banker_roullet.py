import random
names_string = "Nivi, Lila, Stete, Ben, Marry"
names = names_string.split(", ")

num_items = len(names)
random_position = random.randint(0, num_items - 1)
print(f"{names[random_position]} will pay the bill today!")


