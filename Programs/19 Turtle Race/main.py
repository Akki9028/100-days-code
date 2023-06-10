import turtle as t
import random
# import colorgram

screen = t.Screen()
screen.setup(width=500, height=400)
bet_turtle = screen.textinput(
  title="Make your bet",
  prompt="which turtle will run the race? Enter a color: ")
print(f"your bet {bet_turtle}")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
x = -240
y = -150
for color in colors:
  new_turtle = t.Turtle(shape="turtle")
  new_turtle.penup()
  y = y + 50
  new_turtle.goto(x=x, y=y)
  new_turtle.color(color)
  turtle_list.append(new_turtle)

while True:
  move_turtle = random.choice(turtle_list)
  move_turtle.forward(1)
  #print(move_turtle.xcor())
  if move_turtle.xcor() >= 230:
    if bet_turtle == move_turtle.pencolor():
      print(f"You won. {move_turtle.pencolor()} win the race.")
    else:
      print(f"You lose. {move_turtle.pencolor()} win the race.")
    break

screen.exitonclick()
