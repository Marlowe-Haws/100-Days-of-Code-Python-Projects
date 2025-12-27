from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 1
    if timer:
        window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checks_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def update_reps():
    global reps
    if reps < 8 and reps % 2 != 0:
        checks_label.config(text="✓" * (math.ceil(reps/2)))
    reps += 1
    start_timer()

def start_timer():
    global reps
    if reps > 8:
        timer_label.config(text="Finished!", fg=GREEN)
        reps = 1
        return
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        update_reps()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

checks_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checks_label.grid(column=1, row=3)

window.mainloop()

# Practice, assigning command after 1 second wait, calling function
# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# window.after(1000, say_something, 3, 5, 8)
