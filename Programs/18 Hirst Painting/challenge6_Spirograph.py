import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
#tim.pensize(10)
t.colormode(255)

# colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black"]


def getcolor():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color = (r, g, b)
  return color


def draw_shape(gap):
  for _ in range(0, int(360 / gap)):
    tim.color(getcolor())
    tim.circle(100)
    tim.setheading(tim.heading() + gap)


draw_shape(5)

screen = t.Screen()
screen.exitonclick()
