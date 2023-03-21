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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# we will place an image on canvas, so it should be ~ the same size
canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png") #to transform png image to smth canvas unredstands
canvas.create_image(102, 112, image=tomato)
canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=2, row=2)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer.grid(column=2, row=1)

start = Button(text="Start", padx=5, pady=5)
reset = Button(text="Reset", padx=5, pady=5)
start.grid(column=1, row=3)
reset.grid(column=3, row=3)

check = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check.grid(column=2, row=4)

window.mainloop()