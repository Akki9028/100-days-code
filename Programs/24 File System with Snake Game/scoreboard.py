from turtle import Turtle

SCOREBOARD_FONT = ('Arial', 20, 'normal')
SCOREBOARD_ALIGN = "center"


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.highscore = 0
    self.color("white")
    self.penup()
    self.goto(0, 270)
    self.readhighScore()
    self.write(f"Score: {self.score} HighScore: {self.highscore}",
               False,
               align=SCOREBOARD_ALIGN,
               font=SCOREBOARD_FONT)
    self.hideturtle()
    

  def readhighScore(self):
    with open("HighScore.txt") as file:
      self.highscore = int(file.read())

  def writehighscore(self):
    with open("HighScore.txt",mode="w") as file:
      file.write(str(self.score))

  def increasescore(self):
    self.score += 1
    self.clear()
    self.write(f"Score: {self.score} HighScore: {self.highscore}",
               False,
               align=SCOREBOARD_ALIGN,
               font=SCOREBOARD_FONT)

  def reset(self):
    if self.score > self.highscore:
      self.highscore = self.score
      self.writehighscore()
    self.score = 0
    self.clear()
    self.write(f"Score: {self.score} HighScore: {self.highscore}",
               False,
               align=SCOREBOARD_ALIGN,
               font=SCOREBOARD_FONT)

  # def game_over(self):
  #   self.goto(0,0)
  #   self.write("Game Over", align=SCOREBOARD_ALIGN, font=SCOREBOARD_FONT)
