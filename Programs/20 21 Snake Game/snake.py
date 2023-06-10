import turtle as t
MOVE_DISTANCE = 20

class Snake:
  def __init__(self):
    self.turtle_list = []
    self.create_snake()
    self.head= self.turtle_list[0]

  def create_snake(self):
    startx=0
    starty=0
    for body in range(3):
      new_turtle = t.Turtle(shape="square")
      new_turtle.penup()
      new_turtle.color("white")
      startx=startx-20
      new_turtle.goto(x=startx,y=starty)
      self.turtle_list.append(new_turtle)

  def move(self):
    for turtle in range(len(self.turtle_list)-1,0,-1):
      new_x = self.turtle_list[turtle-1].xcor()
      new_y = self.turtle_list[turtle-1].ycor()
      self.turtle_list[turtle].goto(new_x,new_y)
    self.head.forward(MOVE_DISTANCE) 

  def up(self):
    print("here")
    self.head.setheading(90)

  def down(self):
    self.head.setheading(270)

  def left(self):
    self.head.setheading(180)

  def right(self):
    self.head.setheading(0)

  def add_turtle(self):
    new_turtle = t.Turtle(shape="square")
    new_turtle.penup()
    new_turtle.color("white")    
    new_turtle.goto(self.turtle_list[-1].position())
    self.turtle_list.append(new_turtle)
    
  def extend_snake(self):
    self.add_turtle()
    
  