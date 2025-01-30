from tkinter import *


def convert():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometer_result.config(text=f"{km}")

window = Tk()
window.title("Mile To Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=1, column=0)

miles_label = Label(text="Miles")
miles_label.grid(row=2, column=0)

is_equal_label = Label(text="Is Equal to")
is_equal_label.grid(row=0, column=1)

kilometer_result = Label(text="0")
kilometer_result.grid(row=1, column=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=2, column=1)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(row=1, column=2)

window.mainloop()