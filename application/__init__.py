# flask app
from flask import Flask
app = Flask(__name__)


# database connectivity and ORM
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    # TODO: change db name at some point
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///questions.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


# logging in
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in to use this functionality."


# roles in login_required
from functools import wraps


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role.name == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


# functionalities of this app
from application import views

from application.subjects import models
from application.subjects import views

from application.questions import models
from application.questions import views

from application.auth import models
from application.auth import views


# login functionality pt 2
from application.auth.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# database creation
try:
    db.create_all()
except:
    pass
