from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

#------------------------ UI ----------------------------#
window = Tk()
window.title("Flash-Cards Hu-En")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card = PhotoImage(file="images/card_front.png") #to transform png image to smth canvas unredstands
canvas.create_image(400, 265, image=card)
canvas.grid(column=1, row=1, columnspan=2)

right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

right = Button(image=right, highlightthickness=0)
wrong = Button(image=wrong, highlightthickness=0)
right.grid(column=2, row=2)
wrong.grid(column=1, row=2)


window.mainloop()
