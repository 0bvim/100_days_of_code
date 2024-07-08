# Return as an early exit
def format_name(f_name, l_name):
    #this 3 pairs of double quotes are docstring
    """Take a first a last name and format it to return
    the title case version of the 'full' name."""
    if f_name == "" or l_name == "":
        return "Provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("Tell me your first name? "), input("Now, your last name? ")))
