# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from random import shuffle, choice, randint
import pyperclip


def generate_password():
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"
    ]

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    symbols = ["!", "#", "$", "%", "&", "*", "+", "(", ")"]

    password_letters = [choice(letters) for _ in range(0, randint(4, 7))]

    password_symbols = [choice(numbers) for _ in range(0, randint(3, 4))]

    password_numbers = [choice(symbols) for _ in range(0, randint(3, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
import json


def save_password():
    global entry_website, entry_email, entry_password

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website: {"email": email, "password": password}}

    if len(entry_website.get()) == 0 or len(entry_password.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("C:/Users/Eamin/PycharmProjects/100-days-of-code/Intermediate/day-29/data.json",
                      mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("C:/Users/Eamin/PycharmProjects/100-days-of-code/Intermediate/day-29/data.json",
                      "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("C:/Users/Eamin/PycharmProjects/100-days-of-code/Intermediate/day-29/data.json",
                      mode="w") as data_file:

                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


def find_password():
    website = entry_website.get()
    try:
        with open("C:/Users/Eamin/PycharmProjects/100-days-of-code/Intermediate/day-29/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showerror(title="ERROR", message=f"Invalid {website} Name")


# # ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#343637")

canvas = Canvas(width=200, height=200, bg="#343637", highlightthickness=0)
img = PhotoImage(file="C:/Users/Eamin/PycharmProjects/100-days-of-code/Intermediate/day-29/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:", bg="#343637", fg="#A1DDF2")
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username :", bg="#343637", fg="#A1DDF2")
label_email.grid(row=2, column=0)

label_password = Label(text="Password:", bg="#343637", fg="#A1DDF2")
label_password.grid(row=3, column=0)

entry_website = Entry(width=40)
entry_website.grid(row=1, column=1)
entry_website.focus()

entry_email = Entry(width=40)
entry_email.grid(row=2, column=1)
entry_email.insert(0, "eamin@gmail.com")

entry_password = Entry(width=40)
entry_password.grid(row=3, column=1)

button_generate_pass = Button(text="Generate Password", command=generate_password, bg="#D3933A", fg="white")
button_generate_pass.grid(row=3, column=2, padx=3, sticky="w")

button_generate_search = Button(text="Search", width=13, bg="blue", fg="white", command=find_password)
button_generate_search.grid(row=1, column=2, ipadx=4)

button_add = Button(text="Add", width=33, command=save_password, bg="#D3933A", fg="white")
button_add.grid(row=4, column=1)

window.mainloop()
