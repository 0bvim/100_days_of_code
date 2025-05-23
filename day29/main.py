from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_website():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data file found.")
    else:
        if data.get(website) is None:
            messagebox.showinfo(title="Oops", message="No details for the website exists.")
        else:
            messagebox.showinfo(title="Found!", message=f"Website: {website}\nEmail: {data[website]['email']}\nPassword: {data[website]['password']}")
    finally:
            website_entry.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    password = ""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    for _ in range(12):
        password += random.choice(characters)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy the password to clipboard
    messagebox.showinfo(title="Password", message="Password copied to clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.focus()
email_entry.insert(0, "mage@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_entry.focus()

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
generate_password_button.focus()

search_button = Button(text="Search", command=search_website)
search_button.grid(row=1, column=3)
search_button.focus()

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
add_button.focus()



window.mainloop()
