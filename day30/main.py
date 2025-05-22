#FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("This is a new file")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist in the dictionary")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is and error that I made up.")

height = float(input("Height in m: "))
weight = int(input("Weight in kg: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / (height ** 2)
print(bmi)
