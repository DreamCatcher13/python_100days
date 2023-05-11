from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#import sqlite3

db = SQLAlchemy()

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books.db"
db.init_app(app)

#db = sqlite3.connect("books-collection.db")
#cursor = db.cursor()  # to interact with db
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
#cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
#db.commit()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #def __repr__(self):
        #return f'{self.title} - {self.author} - {self.rating}/10'
    
#db.create_all()



@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html',  books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        book = Book(title=request.form['title'],
                    author=request.form['author'],
                    rating=request.form['rating'])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template('add.html')

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        book_id = int(request.args.get('id'))
        book_selected = db.get_or_404(Book, book_id)
        book_selected.rating = int(request.form['rating'])
        db.session.commit()
        return redirect(url_for('home'))
    book_id = int(request.args.get('id'))
    book_selected = db.get_or_404(Book, book_id)
    return render_template('edit.html', book=book_selected)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

