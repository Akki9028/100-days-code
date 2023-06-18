from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()


# Button
def button_clicked():
  # my_label["text"]="Button Got Clicked!!"
  input_text = input.get()
  my_label.config(text=input_text)


my_button = Button(text="Click me", command=button_clicked)
my_button.pack()

# Entry Textbox
input = Entry(width=20)
input.insert(END, string="Enter Something")
input.pack()

# Text
text = Text(height=5, width=30)
# Put cursor in textbox
text.focus()
text.insert(END, "This \nis multiline \ntextbox")
text.pack()
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))


# Spinbox
def spinbox_used():
  # gets the current value in spinbox
  print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value
def scale_used(value):
  print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
  # print 1 if on button checked otherwise 0
  print(checked_state.get())


# variable to hold on checked state, o is off 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?",
                          variable=checked_state,
                          command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radio buttns
def radio_used():
  print(radio_state.get())


# variable to hold on to which radio button value is check ed
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1",
                           value=1,
                           variable=radio_state,
                           command=radio_used)
radiobutton2 = Radiobutton(text="Option2",
                           value=2,
                           variable=radio_state,
                           command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
  print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
  listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
