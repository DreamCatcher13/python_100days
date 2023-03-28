from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
LANG = ("Ariel", 40, "italic")
WORD = ("Ariel", 60, "bold")

#------------------------ CHANGING WORDS ON FLASH CARD ----------#
def new_word():
    data = pandas.read_csv("data/hungarian_words.csv")
    words = data.to_dict(orient="records")
    record = random.choice(words)
    hu = record["Hungarian"]
    en = record["English"]
    canvas.itemconfig(word, text=hu)

#------------------------ UI ----------------------------#
window = Tk()
window.title("Flash-Cards Hu-En")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png") 
canvas.create_image(400, 265, image=card_front)
lang = canvas.create_text(400, 150, text="Hungarian", font=LANG)
word = canvas.create_text(400, 270, text="a word", font=WORD)
canvas.grid(column=1, row=1, columnspan=2)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right = Button(image=right_img, highlightthickness=0, command=new_word)
wrong = Button(image=wrong_img, highlightthickness=0, command=new_word)
right.grid(column=2, row=2)
wrong.grid(column=1, row=2)


window.mainloop()
