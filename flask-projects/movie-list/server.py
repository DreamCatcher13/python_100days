from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import EditMovie, AddMovie
import requests

db = SQLAlchemy()

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-movies1.db"
db.init_app(app)
Bootstrap(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    ranking = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(100), unique=True)

#db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()    
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditMovie()
    m_id = request.args.get('id')
    movie = db.get_or_404(Movie, m_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete():
    m_id = request.args.get('id')
    movie = db.get_or_404(Movie, m_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        new_movie = Movie(
            title=form.title.data,
            year=int(form.year.data),
            description=form.description.data,
            ranking=float(form.ranking.data)
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
