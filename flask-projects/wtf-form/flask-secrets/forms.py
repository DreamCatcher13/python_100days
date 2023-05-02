from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
#from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    email = StringField(label='Your email')
    pwd = PasswordField(label='Your password')
    submit = SubmitField(label='Log In')