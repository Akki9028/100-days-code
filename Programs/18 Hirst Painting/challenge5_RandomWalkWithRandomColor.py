import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
tim.pensize(10)
t.colormode(255)

# colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black"]


def getcolor():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color = (r, g, b)
  return color


angle = [0, 90, 180, 270]

for walk in range(500):
  tim.color(getcolor())
  tim.forward(30)
  tim.setheading(random.choice(angle))

screen = t.Screen()
screen.exitonclick()
