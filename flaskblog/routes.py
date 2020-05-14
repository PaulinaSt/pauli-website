from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, NewsletterForm
from flaskblog.models import User, Post, Newsletter
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/') #what we type into our browsers to go to different pages, will handle all the complicated backend stuff, ("/") homepage
@app.route('/home', methods=['GET', 'POST']) #add a second route going to the same page
def home():
    form = NewsletterForm()
    if form.validate_on_submit():
        subscriber = Newsletter(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()
        flash('You have been added to our newsletter list. Thank you', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', title="Newsletter", form=form)

@app.route('/projects') #add about page
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/register', methods=['GET', 'POST']) #add register page
def register():   
    if current_user.is_authenticated:
        return redirect(url_for('home')) 
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',  methods=['GET', 'POST']) #add login page
def login():    
    if current_user.is_authenticated:
        return redirect(url_for('home')) 
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next') #optional
                return redirect(next_page) if next_page else redirect(url_for('home')) #redirect to next page if it exists,if not return to home
            else:
                 flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout') #add logout page
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required #can only access when loggedin
def account():
     return render_template('account.html', title='Account')