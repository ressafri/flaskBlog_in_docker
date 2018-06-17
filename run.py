# Set the PATH
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from app import app
# from forms.forms import RegistrationForm, LoginForm

run = Manager(app)

# Turn on debugger by default and reloader

run.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=5000
))


if __name__ == "__main__":
    run.run()
