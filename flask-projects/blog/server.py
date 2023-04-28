from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

blog_url = 'https://www.jsonkeeper.com/b/HTK6'
all_posts = requests.get(url=blog_url).json()

@app.route('/')
def home():
    y = datetime.now().strftime("%Y")
    # passing value to template
    return render_template('index.html', year=y, posts=all_posts) 

@app.route('/post/<int:id>')
def post(id):
    for p in all_posts:
        if p['id'] == id:
            selected = p
            return render_template("post.html", post=selected)
        

if __name__ == "__main__":
    app.run(debug=True)

#https://jsonkeeper.com/b/HTK6