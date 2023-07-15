import smtplib

my_email = "1@gmail.com"
passward = "cguiiwzimytekpoc"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#   connection.starttls()

#   connection.login(user=my_email, password=passward)
#   connection.sendmail(from_addr=my_email,
#                       to_addrs="99@gmail.com",
#                       msg="Subject: Hello\n\nThis is the body of my email")

# # connection.close()

import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 5:
  with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)

  print(quote)
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()

    connection.login(user=my_email, password=passward)
    connection.sendmail(from_addr=my_email,
                        to_addrs="99@gmail.com",
                        msg=f"Subject: Monday Motivation\n\n{quote}")
