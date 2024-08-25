PLACEHOLDER = "[name]"

with open("input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("input/Letters/letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        final_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, final_name)
        with open(f"./output/ReadyToSend/letter_for_{final_name}.docx", mode = "w") as completed_letter:
            completed_letter.write(new_letter)
