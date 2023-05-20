import random

print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")

level = input("Choose a difficulty level. Type 'easy' or 'hard':")

if level == "easy":
  attempts = 10
else:
  attempts = 5

while attempts > 0:
  print(f"Your have {attempts} attempts remaining to guess a number.")
  guess = int(input("Make a guess:"))

  if guess > number:
    print("Too high.")
    print("Guess again")
  elif guess < number:
    print("Too low.")
    print("Guess again")
  else:
    print(f"You got it! The number was {number}")
    break
  attempts -= 1

if attempts == 0:
  print("You are out of aattempts. You lose..!!")
