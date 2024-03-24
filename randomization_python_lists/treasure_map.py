line1 = ["0", "0", "0"]
line2 = ["0", "0", "0"]
line3 = ["0", "0", "0"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where you want to put the treasure? ")
# my code
#if position[0].lower() == "a":
#    position1 = 0
#elif position[0].lower()== "b":
#    position1 = 1
#elif position[0].lower() == "c":
#    position1 = 2
#position2 = int(position[1]) - 1
# class code
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
# if you try to run my code remember to change number_index and letter_index for position1 and 2
map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")
