from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
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
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        Timer(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        Timer(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        Timer(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def Timer(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, Timer, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔️"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

# * canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", font=(
    FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)


# * Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=0, column=1)

# * Start Button
start_btn = Button(text="start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

# * Reset Button
reset_btn = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

# * Check Label
check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)


window.mainloop()
