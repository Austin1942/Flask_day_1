from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo 
from app.models import User




class CheckForm(FlaskForm):
    psearch = StringField('What Pokemon are you looking for?', validators=[DataRequired()])
    submit = SubmitField('Search')