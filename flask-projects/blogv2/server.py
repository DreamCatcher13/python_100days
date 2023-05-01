from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = 'https://www.jsonkeeper.com/b/HTK6'
all_posts = requests.get(url=blog_url).json()

@app.route('/')
def home():
    return render_template('index.html', posts=all_posts) 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
    for p in all_posts:
        if p['id'] == id:
            selected = p
    return render_template("post.html", post=selected)
        

if __name__ == "__main__":
    app.run(debug=True)