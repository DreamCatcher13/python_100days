from flask import Flask
import random

app = Flask(__name__)

url1 = "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif"
url2 = "http://metaf.tumblr.com/post/61633057663"
number = random.randint(0, 9)

@app.route('/')
def hello():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/K1tgb1IUeBOgw/giphy.gif" >'

@app.route("/<int:n>")
def result(n):
    if n < number:
        return '<h1 style="color: red">Too low, try again</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" >'
    elif n > number:
        return '<h1 style="color: purple">Too high, try again</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" >'
    else:
        return '<h1 style="color: green">Correct</h1>' \
               '<img src="https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif" >'

if __name__ == "__main__":
    app.run(debug=True)