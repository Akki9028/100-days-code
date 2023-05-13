#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator!")
Bill = int(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
peoples = int(input("How many people to split the bill?"))

#Each person should pay (150.00 / 5) * 1.12 = 33.6
totalBill = Bill + (Bill * tip / 100)
eachBill = totalBill / peoples
print(eachBill)
#Format the result to 2 decimal places = 33.60
finalamount = "{:.2f}".format(eachBill)
print(finalamount)

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
