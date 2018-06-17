from flask import Flask, render_template, url_for, flash, redirect
from app import app
from forms import *
from forms.forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = '8d4166e680b666960a70d96868024095'

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
