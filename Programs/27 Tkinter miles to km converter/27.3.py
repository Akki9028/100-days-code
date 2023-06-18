from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=200,y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button
def button_clicked():
  # my_label["text"]="Button Got Clicked!!"
  input_text = input.get()
  my_label.config(text=input_text)


my_button = Button(text="Click me", command=button_clicked)
# my_button.pack()
my_button.grid(column=1, row=1)

# Entry Textbox
input = Entry(width=20)
input.insert(END, string="Enter Something")
# input.pack()
input.grid(column=2, row=2)

window.mainloop()
