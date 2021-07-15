from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_ruselt_label.config(text=f"{round(km)}  km")

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=290, height=100)
window.config(padx=20, pady=20)

# Creating a label

my_label = Label(text='Miles :', font=("Arial", 12))

miles_input = Entry(width=20)

new_label = Label(text='in kilometer:', font=("Arial", 12))

kilometer_ruselt_label = Label(text=f'0  km', font=("Arial", 10))

button = Button(text="Claculate", command=miles_to_km)




my_label.grid(row=0, column=0)
miles_input.grid(row=0, column=1)
new_label.grid(row=1, column=0)
kilometer_ruselt_label.grid(row=1, column=1)
button.grid(row=4, column=1)





window.mainloop()
