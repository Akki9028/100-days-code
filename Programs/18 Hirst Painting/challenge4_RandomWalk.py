from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")
#Print
import random

colors = [
  "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple",
  "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green",
  "darkgreen", "chocolate", "brown", "black"
]

angle = [0, 90, 180, 270]

for walk in range(1000):
  tim.color(random.choice(colors))
  tim.pensize(10)
  tim.forward(30)
  tim.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()
