import requests, os, sys
from datetime import datetime
from tkinter import *
from tkinter import messagebox

### for pyinstaller ###
def resource_path(relative_path):
    try:   
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

with open("token.txt", "r") as f:
    content = [l.rstrip() for l in f.readlines()]
    TOKEN, USERNAME = content[0], content[1]

PIXELA = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
NOW = datetime.now().strftime("%Y%m%d")
HEADERS = {
    "X-USER-TOKEN": TOKEN
}
GRAPH_PARAMS = {
    "date": NOW,
    "quantity": "0"
}

""" posting a pixel """
def post_a_pixel():
    username = user.get()
    graph_id = graph.get()
    GRAPH_PARAMS['quantity'] = quantity.get()
    if len(username) == 0 or len(graph_id) == 0 or len( GRAPH_PARAMS['quantity']) == 0:
        messagebox.showinfo(title="Error", message="You should fill all the fields")
    else:
        endpoint = f"{PIXELA}/{username}/graphs/{graph_id}"
        responce = requests.post(url=endpoint, json=GRAPH_PARAMS, headers=HEADERS)
        msg = responce.json()
        messagebox.showinfo(title="Responce", message=msg['message'])

### GUI ###
window = Tk()
window.title("Pixela habit tracker")
window.config(padx=15, pady=15)

canvas = Canvas(width=480, height=270, highlightthickness=0)
parrot = PhotoImage(file=resource_path("pixela.png"))
canvas_img = canvas.create_image(240, 135, image=parrot)
canvas.grid(column=1, row=2, columnspan=3)

title = Label(text="Add a pixel :)", justify="center", font=("Agency FB", 18))
title.grid(column=2, row=1)

t_user = Label(text="Enter your username", font=("Agency FB", 14))
t_graph = Label(text="Enter your graph ID", font=("Agency FB", 14))
t_quantity = Label(text="Enter quantity", font=("Agency FB", 14))
t_user.grid(column=1, row=3)
t_graph.grid(column=1, row=4)
t_quantity.grid(column=1, row=5)

user = Entry(width=20)
user.insert(0, USERNAME)
graph = Entry(width=20)
graph.insert(0, GRAPH_ID)
quantity = Entry(width=20)
user.grid(column=2, row=3)
graph.grid(column=2, row=4)
quantity.grid(column=2, row=5)

add_pixel = Button(text="Add a pixel",
                   width=15,
                   command=post_a_pixel)
add_pixel.grid(column=3, row=4)


window.mainloop()


""" creating user 
endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

responce = requests.post(url=endpoint, json=user_params)
print(responce.text) 
"""

""" creating a graph
endpoint = f"{pixela}/{username}/graphs"
headers = {
    "X-USER-TOKEN": token
}

graph_params = {
    "id": "graph1",
    "name": "Python coding",
    "unit": "minutes",
    "type": "int",
    "color": "momiji"
}
responce = requests.post(url=endpoint, json=graph_params, headers=headers)
print(responce.text)
"""

""" update a pixel 
headers = {
    "X-USER-TOKEN": token
}

date = datetime.now().strftime("%Y%m%d")

graph_params = {
    "quantity": "110"
}

endpoint = f"{pixela}/{username}/graphs/{graph_id}/{date}"
# PUT method !
responce = requests.put(url=endpoint, json=graph_params, headers=headers)
print(responce.text) 
"""