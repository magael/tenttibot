# flask app
from flask import Flask
app = Flask(__name__)

# database
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    # notice: at the moment the app needs one initial subject in the db in order for most functionality
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///questions.db" # change the name at some point?
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# functionalities of this app
from application import views

from application.subjects import models
from application.subjects import views

from application.questions import models
from application.questions import views

from application.auth import models
from application.auth import views

# logging in
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# create tables when necessary
try: 
    db.create_all()
except:
    pass