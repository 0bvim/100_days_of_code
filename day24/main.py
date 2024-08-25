# this way you need to close file manually
# file = open("my_file.txt")

# print(file.read())

# file.close()

# with this keywords the system do it automatically
with open("my_file.txt") as file:
    print(file.read())

# to write in a file you need to change default mode (read) to write or to append
with open("my_file.txt", mode="a") as file:
    file.write("Hello darkness my old friend\n")

with open("my_file.txt") as file:
    print(file.read())
