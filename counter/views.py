from counter.models import User, Post
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from app import app
from forms.forms import RegistrationForm, LoginForm
# from forms import *
# from forms.forms import RegistrationForm, LoginForm
db = SQLAlchemy(app)

posts = [
    {
        'author': 'redwan essafri',
        'title': 'Blog post 1',
        'content': 'fist post content',
        'date_posted': 'May 15, 2018'
    },

    {
        'author': 'Mariam Essafri',
        'title': 'Blog post 2',
        'content': 'fist post content',
        'date_posted': 'May 14, 2018'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='home')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'me@ee.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unseccusseful, please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
