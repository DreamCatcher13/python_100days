from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField(label='Your email', validators=[DataRequired(), Email()])
    pwd = PasswordField(label='Your password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')