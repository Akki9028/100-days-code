import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#   print(x, y)
# turtle.onclick(get_mouse_click_coor)

states_data = pandas.read_csv("50_states.csv")
print(states_data)
states_count = len(states_data.state)

guess_states = []
remaining_states = []

while len(guess_states) < states_count:
  answer_state = screen.textinput(
    title=f"{len(guess_states)} /50 Guessed correct",
    prompt="What's another state's name?")

  print(answer_state)

  formatted_ans = answer_state.title()

  if formatted_ans == "Exit":
    for state in states_data.state:
      if state not in guess_states:
        remaining_states.append(state)
    print(remaining_states)
    break
  states_count = len(states_data.state)

  if formatted_ans in states_data.state.to_list():
    data = states_data[states_data.state == formatted_ans]
    guess_states.append(formatted_ans)
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(int(data.x), int(data.y))
    t.write(data.state.item())

  # def print_state_on_screen(x , y, ans):
  #   t = turtle.Turtle()
  #   t.penup()
  #   t.hideturtle()
  #   t.goto(x,y)
  #   t.write(ans)

  # print_state_on_screen(int(data.x), int(data.y), formatted_ans)

# screen.exitonclick()
