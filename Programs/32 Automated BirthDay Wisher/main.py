import smtplib
import pandas
from datetime import datetime
import random

# my_email = "1@gmail.com"
# passward = "cguiiwzimytekpoc"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#   connection.starttls()

#   connection.login(user=my_email, password=passward)
#   connection.sendmail(from_addr=my_email,
#                       to_addrs="99@gmail.com",
#                       msg="Subject: Hello\n\nThis is the body of my email")

# # connection.close()

# import datetime as dt
# import random

# now = dt.datetime.now()
# weekday = now.weekday()
# print(weekday)
# if weekday == 5:
#   with open("quotes.txt") as file:
#     all_quotes = file.readlines()
#     quote = random.choice(all_quotes)

#   print(quote)
#   with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()

#     connection.login(user=my_email, password=passward)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="99@gmail.com",
#                         msg=f"Subject: Monday Motivation\n\n{quote}")

now = datetime.now()
today_date = (now.month, now.day)

print(today_date)

data = pandas.read_csv("birthdays.csv")
print(data)

birthday_dict = {(data_row.month, data_row.day): data_row
                 for index, data_row in data.iterrows()}

if today_date in birthday_dict:
  birthday_person = birthday_dict[today_date]
  letter_path = f"Letters_template/Letter{random.randint(1,3)}.txt"

  with open(letter_path) as letter_file:
    context = letter_file.read()
    context = context.replace("[NAME]", birthday_person["name"])

  print(context)
  # with smtplib.SMTP("smtp.gmail.com") as conn:
  #   conn.starttls()
  #   conn.login(EMAIL, PASSWORD)
  #   conn.sendmail(from_addr=EMAIL,
  #                 to_addrs=TO_EMAIL,
  #                 msg=f"Subject:Happy Birthday\n\n{context}")
