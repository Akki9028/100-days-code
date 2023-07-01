# IndexError Handling
# UPDATE
# We've moved away from repl.it for coding exercises. Check out the new exercises on Coding Rooms with automated submissions.

# Login to your Udemy course and head over to lesson 9 to get the sign up link: Click here

# Issue
# We've got some buggy code. Try running the code. The code will crash and give you an IndexError. This is because we're looking through the list of fruits for an index that is out of range.

# Bad Output
# Cannot infer image mime type

# Instructions
# Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie". e.g.

# Cannot infer image mime type

# Hint
# You'll need to catch the IndexError exception.

# You'll need the try, except and else keywords.

# Test Your Code
# Before checking the solution, try copy-pasting your code into this repl:

# https://repl.it/@appbrewery/day-30-1-test-your-code

# This repl includes my testing code that will check if your code meets this assignment's objectives.

# Solution
# https://repl.it/@appbrewery/day-30-1-solution


fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
      fruit = fruits[index]
      # print(fruit + " pie")
    except IndexError:
      print("Fruit Pie")
    else:
      print(fruit + " pie")
make_pie(4)