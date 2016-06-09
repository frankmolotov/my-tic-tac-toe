from flask_wtf import Form
from wtforms import TextField, BooleanField, StringField, validators, PasswordField

class RegistrationForm(Form):
	username = StringField('username', [validators.Length(min=4, max=25)])
	email = StringField('email', [validators.Email()])
	password = PasswordField('password', [validators.DataRequired(),
	validators.EqualTo('confirm',
	message='Passwords must match')])
	confirm = PasswordField('Repeat password')

class LoginForm(Form):
	email = StringField('username', [validators.Length(min=4, max=25),])
	password = PasswordField('password')
