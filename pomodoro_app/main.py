from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timet_text, text="00:00")
    check.config(text="")
    global repetitions
    repetitions = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetitions
    repetitions += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec =  LONG_BREAK_MIN * 60

    if repetitions % 8 == 0:
        timer.config(text="Long break", fg=RED)
        count_down(long_break_sec)
    elif repetitions % 2 == 0:
        timer.config(text="Short break", fg=PINK)
        count_down(short_break_sec)
    else: 
        timer.config(text="Work", fg=GREEN)   
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = int(count / 60)
    sec = int(count % 60)

    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"

    canvas.itemconfig(timet_text, text=f"{min}:{sec}") #config canvas element
    if count > 0:
        global my_timer
        #recursion, after 1000 ms = 1 s, call count_down func with arg
        my_timer = window.after(1000, count_down, count-1) 
    else:
        start_timer()
        marks = "" #every time we finish work marks became empty
        work_session = int(repetitions/2)
        for _ in range(work_session):
            marks += "✓" #first it will add 1 check, next 2 and so on
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# we will place an image on canvas, so it should be ~ the same size
canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png") #to transform png image to smth canvas unredstands
canvas.create_image(102, 112, image=tomato)
timet_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=2, row=2)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer.grid(column=2, row=1)

start = Button(text="Start", padx=5, pady=5, command=start_timer)
reset = Button(text="Reset", padx=5, pady=5, command=reset_timer)
start.grid(column=1, row=3)
reset.grid(column=3, row=3)

check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check.grid(column=2, row=4)

window.mainloop()