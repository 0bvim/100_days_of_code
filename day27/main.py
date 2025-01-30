from tkinter import *

window = Tk()
window.title("My First Gui Program")
window.minsize(500, 300)

my_label = Label(text="Label Text", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    my_label.config(text=input.get())

# button
button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()


window.mainloop()