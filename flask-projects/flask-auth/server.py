from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        pwd = generate_password_hash(
            password=request.form['password'],
            method='pbkdf2:sha256',
            salt_length=8
        )
        if User.query.filter_by(email=request.form['email']).first():
            flash('Email already exist')
            return render_template('register.html')
        else:
            user = User(
                email=request.form['email'],
                name=request.form['name'],
                password=pwd
            )
            db.session.add(user)
            db.session.commit()
            login_user(user) #login new user
            return redirect(url_for('secrets', user=user.name))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form['email']).first()
        if not user:
            return redirect(url_for('register'))
        pwd_match = check_password_hash(user.password, request.form['password'])
        if pwd_match:
            login_user(user)
            #flash('Logged in successfully')
            return redirect(url_for('secrets'))
        else:
            flash("Password doesn't match")
            return render_template("login.html")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user=current_user.name.capitalize())


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'files/cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
