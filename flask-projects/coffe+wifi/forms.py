from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location on Google Maps Url', validators=[DataRequired(), URL()])
    open_time = StringField('Opening time, e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing time, e.g. 8PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=[('☕️'), ('☕️☕️'), ('☕️☕️☕️'), ('☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️')], validators=[DataRequired()])
    wifi = SelectField('WiFi strength Rating', choices=[('✘'), ('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')], validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=[('✘'), ('🔌'), ('🔌🔌'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')