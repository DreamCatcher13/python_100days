from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
LANG = ("Ariel", 40, "italic")
WORD = ("Ariel", 60, "bold")

try: 
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/hungarian_words.csv")

words = data.to_dict(orient="records") # to get list of dictionary records
record = {}

#------------------------ CHANGING WORDS ON FLASH CARD ----------#
def new_word():
    global record, flip_timer
    window.after_cancel(flip_timer) 
    record = random.choice(words)
    canvas.itemconfig(canvas_img, image=card_front)
    canvas.itemconfig(lang, fill="black", text="Hungarian")    
    canvas.itemconfig(word, fill="black", text=record["Hungarian"])
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(lang, fill="white",  text="English")    
    canvas.itemconfig(word, fill="white", text=record["English"])

def known_word():
    words.remove(record)
    unknown_words = pandas.DataFrame(words)
    unknown_words.to_csv("data/words_to_learn.csv", index=False)
    new_word()

#------------------------ UI ----------------------------#
window = Tk()
window.title("Flash-Cards Hu-En")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card) #for the first card

canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png") 
card_back = PhotoImage(file="images/card_back.png") 
canvas_img = canvas.create_image(400, 265, image=card_front)
lang = canvas.create_text(400, 150, font=LANG)
word = canvas.create_text(400, 270, font=WORD)
canvas.grid(column=1, row=1, columnspan=2)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right = Button(image=right_img, highlightthickness=0, command=known_word)
wrong = Button(image=wrong_img, highlightthickness=0, command=new_word)
right.grid(column=2, row=2)
wrong.grid(column=1, row=2)

new_word()

window.mainloop()
