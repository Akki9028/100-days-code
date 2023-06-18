from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random


def generate_password():
  letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  ]
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters = [random.choice(letters) for _ in range(nr_letters)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

  password_list = password_letters + password_numbers + password_symbols
  random.shuffle(password_list)

  # password = ""
  # for char in password_list:
  #   password += char

  password = "".join(password_list)
  # print(f"Your password is: {password}")

  password_input.delete(0, END)
  password_input.insert(0, password)
  # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  website = website_input.get()
  email_username = email_username_input.get()
  password = password_input.get()

  if len(website.strip()) > 0 and len(password.strip()) > 0:
    is_ok = messagebox.askokcancel(
      title=website,
      message=
      f"These are the details entered: \nEmail: {email_username} \nPassword: {password} \nis it okay to save?"
    )

    if is_ok:
      with open(file="data.txt", mode="a") as file:
        file.write(f"{website} | {email_username} | {password} \n")
      website_input.delete(0, END)
      password_input.delete(0, END)

  else:
    messagebox.showerror(title="Oops",
                         message="Please don't leave any fields empty.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.config(width=600, height=450)
window.config(padx=20, pady=20)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=40)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry(width=40)
email_username_input.insert(0, "akkipatil@gmail.com")
email_username_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=22)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add to file", width=40, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

# window.mainloop()
