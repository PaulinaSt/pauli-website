from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, NewsletterForm
from flaskblog.models import User, Post, Newsletter
from flaskblog.functions import login, register, home
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/') #what we type into our browsers to go to different pages, will handle all the complicated backend stuff, ("/") homepage
@app.route('/home', methods=['GET', 'POST']) #add a second route going to the same page
def home()


@app.route('/projects') #add about page
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/register', methods=['GET', 'POST']) #add register page
def register()

@app.route('/login',  methods=['GET', 'POST']) #add login page
def login()

@app.route('/logout') #add logout page
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required #can only access when loggedin
def account():
     return render_template('account.html', title='Account')