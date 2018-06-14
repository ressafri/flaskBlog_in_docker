from app import app


@app.route("/")
@app.route("/home")
def home():
    return "<h1>This is the home page</h1>"

# app.config.from_object('settings')


@app.route("/about")
def about():
    return "<h1>about me</h1>"
