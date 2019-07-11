from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField
from wtforms.validators import InputRequired,DataRequired,Email

class register(FlaskForm):
	name=StringField('Name',validators=[DataRequired()])
	email=StringField('Email',validators=[DataRequired(),Email()])
	phone=IntegerField('Phone Number',validators=[DataRequired()])
	msg=StringField('Message',)
