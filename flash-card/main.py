from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

#------------------------ UI ----------------------------#
window = Tk()
window.title("Flash-Cards Hu-En")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card = PhotoImage(file="images/card_front.png") 
canvas.create_image(400, 265, image=card)
canvas.grid(column=1, row=1, columnspan=2)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right = Button(image=right_img, highlightthickness=0)
wrong = Button(image=wrong_img, highlightthickness=0)
right.grid(column=2, row=2)
wrong.grid(column=1, row=2)


window.mainloop()
