from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'mykey'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)