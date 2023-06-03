from turtle import Turtle, Screen

tim = Turtle()
# tim.setpos(20,20)

#Print dashed line
# for _ in range(15):
#   tim.forward(10)
#   tim.penup()
#   tim.forward(10)
#   tim.pendown()

#Print
import random

colors = [
  "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple",
  "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green",
  "darkgreen", "chocolate", "brown", "black"
]

for sides in range(3, 11):
  angle = 360 / sides
  tim.color(random.choice(colors))
  for _ in range(sides):
    tim.forward(100)
    tim.right(angle)

screen = Screen()
screen.exitonclick()
