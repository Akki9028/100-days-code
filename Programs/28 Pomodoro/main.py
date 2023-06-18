# ----------------------------------
# POMODORO
# 25 min work
# 5 min break
# 25 min work
# 5 min break
# 25 min work
# 5 min break
# 25 min work
# 20 min long break

# ----------------------------------

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Ubuntu Mono"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text="00:00")
  timer_label.config(text="Timer")
  check_label.config(text="")
  global resp
  resp = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
  global reps
  reps += 1

  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  if reps % 8 == 0:
    count_down(long_break_sec)
    timer_label.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    count_down(short_break_sec)
    timer_label.config(text="Break", fg=PINK)
  else:
    count_down(work_sec)
    timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
  # 00:00
  count_minute = math.floor(count / 60)
  if count_minute < 10:
    count_minute = f"0{count_minute}"

  count_second = count % 60
  if count_second < 10:
    count_second = f"0{count_second}"
  canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    mark = ""
    work_sessions = math.floor(reps / 2)
    for _ in range(work_sessions):
      mark += "✔"
      check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer",
                    fg=GREEN,
                    bg=YELLOW,
                    font=(FONT_NAME, 24, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=205, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 115, image=tomato_img)
timer_text = canvas.create_text(103,
                                130,
                                text="00:00",
                                fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
