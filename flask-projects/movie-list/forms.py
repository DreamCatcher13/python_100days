from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class EditMovie(FlaskForm):
    rating = StringField('Movie rating', validators=[DataRequired()])
    review = StringField('Movie review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddMovie(FlaskForm):
    title = StringField('Movie name', validators=[DataRequired()])
    year = StringField('Movie year', validators=[DataRequired()])
    description = StringField('Movie description', validators=[DataRequired()])
    ranking = StringField('Movie ranking', validators=[DataRequired()])
    submit = SubmitField('Submit')