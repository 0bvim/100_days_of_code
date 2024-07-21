# def format_name(f_name, l_name):
#     ff_name = f_name.title()
#     fl_name = l_name.title()
#
#     return f"{ff_name} {fl_name}"
#
# print(format_name("estephany", "freiTaS"))

# multiple returns
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Wrong input, bye."
    ff_name = f_name.title()
    fl_name = l_name.title()

    return f"{ff_name} {fl_name}"


print(format_name(input("First name: "), input("Last Name: ")))
