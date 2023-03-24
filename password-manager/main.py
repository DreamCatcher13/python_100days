from tkinter import *
from tkinter import messagebox
import string, random, pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    min_length = random.randint(10, 12)
    all_char = letters + digits + special
    pwd = ""
    while len(pwd) != min_length:
        new_char = random.choice(all_char)
        pwd += new_char
    password_out.delete(0, END)
    password_out.insert(0, pwd)
    pyperclip.copy(pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    s = site.get()
    em = user_email.get()
    p = password_out.get()

    if len(s) == 0 or len(p) == 0 or len(em) == 0:
        messagebox.showerror(title="Manager error", message="Don't leave any of the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"{s}",
                                message=f"You are going to save this: \nEmail: {em}, \nPassword: {p} \nIs this ok?")
        if is_ok:
            with open("pwd.txt", "a") as file:
                file.write(f"{s} | {em} | {p}\n") #yes, it is not encrypted :)
            site.delete(0, END) # clear all field
            password_out.delete(0, END)
            site.focus()

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
user_email = Entry(width=40)
password_out = Entry(width=40)
site.grid(column=2, row=2)
site.focus() # put cursor in the field 
user_email.grid(column=2, row=3)
user_email.insert(0, "mybox@mail.com") # 0 and END are indecies, there you put your string
password_out.grid(column=2, row=4)

generate = Button(text="Generate password", command=generate_password)
add_pass = Button(text="Add", width=35, command=save_pass)
generate.grid(column=3, row=4)
add_pass.grid(column=2, row=5)

window.mainloop()