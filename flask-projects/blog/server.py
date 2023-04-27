from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    y = datetime.now().strftime("%Y")
    # passing value to template
    return render_template('index.html', year=y) 

@app.route("/guess/<name>")
def guess(name):
    agify = requests.get(f"https://api.agify.io?name={name}")
    genderize = requests.get(f"https://api.genderize.io?name={name}")
    age = str(agify.json()['age'])
    gender = genderize.json()['gender']
    return render_template('api.html', n=name, a=age, g=gender)

@app.route("/blog")
def blog():
    # can't access npoint
    blog_url = 'https://api.npoint.io/5abcca6f4e39b4955965'
    all_posts = requests.get(url=blog_url)
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)