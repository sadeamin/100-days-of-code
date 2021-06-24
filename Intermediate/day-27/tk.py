from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=400, height=200)

# Creating a label

my_label = Label(text='I Am a label', font=("Arial", 14))
my_label.grid(row=0, column=0)

my_label["text"] = "New Text"
my_label.config(text="New text")

button = Button(text="Chick me")
button.grid(row=1, column=1)

input = Entry(width=10)
input.grid(row=2, column=3)

button1 = Button(text="Chick me")
button1.grid(row=0, column=2)

window.mainloop()