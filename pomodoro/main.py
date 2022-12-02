from tkinter import *
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
timerr=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timerr)
    timer.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8==0:
        count_down(long_break_sec)
        timer.config(text="BREAK", fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        timer.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="WORK", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    global timerr
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if(count>0):
        timerr = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas=Canvas(width=205, height=230, bg=YELLOW, highlightthickness=0)


tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, fill="white", text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer=Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer.grid(row=0, column=1)

start_button = Button(text="Start",command=start_timer , highlightthickness=0)
start_button.grid(row=2, column=0)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME))
check_mark.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()