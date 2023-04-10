import requests
from datetime import datetime

with open("token.txt", "r") as f:
    content = [l.rstrip() for l in f.readlines()]
    token, username = content[0], content[1]

pixela = "https://pixe.la/v1/users"
graph_id = "graph1"

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

""" posting a pixel """
headers = {
    "X-USER-TOKEN": token
}

now = datetime.now().strftime("%Y%m%d")

graph_params = {
    "date": now,
    "quantity": "60"
}

endpoint = f"{pixela}/{username}/graphs/{graph_id}"

responce = requests.post(url=endpoint, json=graph_params, headers=headers)
print(responce.text) 

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