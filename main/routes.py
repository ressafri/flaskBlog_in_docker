from flask import Flask, render_template
from app import app

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
