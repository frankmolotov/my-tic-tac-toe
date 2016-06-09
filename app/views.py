from flask import render_template, flash, redirect, request
from app.forms import RegistrationForm, LoginForm
from app import app, models, db

@app.route('/')

@app.route('/index')
def index():
    user = { 'nickname': 'Konstantin', 'rating': 0}
    leaders = [ {'nickname': 'John',
				 'points':97},
				 {'nickname': 'Albert',
				 'points':96},
				 {'nickname': 'Valera',
				 'points':99},
				 {'nickname': 'Fedya',
				 'points':97} ]
    return render_template('index.html',user = user,leaders = leaders)
    
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	form = RegistrationForm()
	if request.method == 'POST' and form.validate_on_submit():
		if len(models.User.query.filter_by(username=request.form['username']).all()) > 0:
			flash('User with this name aready registered','error')
			return redirect('/login')
		u = models.User(username = request.form['username'], email = request.form['email'], password = request.form['password'], admin = models.ROLE_USER)
		db.session.add(u)
		db.session.commit()
		flash('Thanks for registering','notification')
		return redirect('/login')
	else:
		error = 'Invalid registration'
	return render_template('register.html', form = form)

@app.route('/login',methods = ['GET','POST'])
def login():
	form = LoginForm()
	if request.method == 'POST' and form.validate_on_submit():
		if len(models.User.query.filter_by(email=request.form['email']).all()) > 0:
			print(models.User.query.filter_by(password=request.form['password']).first())
			print(models.User.query.filter_by(email=request.form['email']).first())
			for user in models.User.query.filter_by(email=request.form['email']).all():
				if request.form['email'] == user.email and request.form['password'] == user.password:
			#if request.form['password'] == models.User.query.filter_by(email=request.form['email']).first().password and request.form['email'] in models.User.query.filter_by(email=request.form['email']).all():
					flash('You were logged in','notification')
					return render_template('index.html',form = form, user = { 'nickname': models.User.query.filter_by(email=request.form['email']).first().username, 'rating': 0})
				else:
					flash('Incorrect password','error')
		flash('Invalid e-mail address','error')
	return render_template('login.html',form = form)
@app.route('/info')
def info():
	info = {'nickname':'allah'}
