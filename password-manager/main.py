from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# we will place an image on canvas, so it should be ~ the same size
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png") #to transform png image to smth canvas unredstands
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

site_name = Label(text="Website:")
user_name = Label(text="Email/Username:")
pass_label = Label(text="Password:")
site_name.grid(column=1, row=2)
user_name.grid(column=1, row=3)
pass_label.grid(column=1, row=4)

site = Entry(width=40)
user = Entry(width=40)
password_out = Entry(width=40)
site.grid(column=2, row=2)
user.grid(column=2, row=3)
password_out.grid(column=2, row=4)

generate = Button(text="Generate password")
add_pass = Button(text="Add", width=35)
generate.grid(column=3, row=4)
add_pass.grid(column=2, row=5)

window.mainloop()