from turtle import Turtle

SCOREBOARD_FONT = ('Arial', 20, 'normal')
SCOREBOARD_ALIGN = "center"

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0,270)
    self.write(f"Score - {self.score}",False,align=SCOREBOARD_ALIGN,font=SCOREBOARD_FONT)
    self.hideturtle()

  def increasescore(self):
    self.score +=1
    self.clear()
    self.write(f"Score - {self.score}",False,align=SCOREBOARD_ALIGN,font=SCOREBOARD_FONT)

  def game_over(self):
    self.goto(0,0)
    self.write("Game Over", align=SCOREBOARD_ALIGN, font=SCOREBOARD_FONT)