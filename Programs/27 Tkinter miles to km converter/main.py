from tkinter import *

window = Tk()
window.title("MIles to Km Converter")
# window.minsize(width=100, height=80)
window.config(padx=20, pady=20)


# Button
def calculate_clicked():
  miles_value = float(input.get())
  km_label.config(text=miles_value * 1.609)


# Entry Textbox
input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=1)

# Miles Label
unit1_label = Label(text="Miles", font=("Arial", 24, "bold"))
unit1_label.grid(column=2, row=1)

# Is equal to
my_label = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=2)

# Km label
km_label = Label(text="0", font=("Arial", 24, "bold"))
km_label.grid(column=1, row=2)

# Km Label
unit2_label = Label(text="Km", font=("Arial", 24, "bold"))
unit2_label.grid(column=2, row=2)

# Calculate buttn
calculate_button = Button(text="Caculate", command=calculate_clicked)
calculate_button.grid(column=1, row=3)

window.mainloop()
