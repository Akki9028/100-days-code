import turtle as t
import random
# import colorgram

# rgb_colors = []
#Extract 30 colors from image
# colors = colorgram.extract("hirst.jpg",30)
# # print(colors)

# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r,g,b)
#   rgb_colors.append(new_color)

# print(rgb_colors)

#verify the colors on w3schools color 
color_list = [(222, 152, 103), (128, 172, 199), (221, 130, 149), (221, 73, 90), (17, 121, 157), (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70), (142, 86, 60), (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213), (1, 98, 119), (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]

tim = t.Turtle()
tim.speed("fastest")
#tim.pensize(10)
t.colormode(255)
tim.penup()
tim.hideturtle()

# colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black"]

# def getcolor():
#   r = random.randint(0,255)
#   g = random.randint(0,255)
#   b = random.randint(0,255)
#   color = (r,g,b)
#   return color

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
def draw_shape(gap):
  for dot in range(1, gap + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot % 10 == 0 :
      tim.setheading(90)
      tim.forward(50)
      tim.setheading(180)
      tim.forward(500)
      tim.setheading(0)        

draw_shape(500)

screen =t.Screen()
screen.exitonclick()
