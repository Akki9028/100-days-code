import turtle as t
import time
import random
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Create snake body
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
  screen.update()
  time.sleep(0.2)
  snake.move()

  #Detect collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.increasescore()
    snake.extend_snake()

  #Detect collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor(
  ) > 280 or snake.head.ycor() < -280:
    scoreboard.game_over()
    break

  #detect collision with snake tail
  for turtle in snake.turtle_list:
    if snake.head == turtle:
      pass
    elif snake.head.distance(turtle) < 10:
      scoreboard.game_over()
      break

screen.exitonclick()
