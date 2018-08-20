from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username", [
        validators.Length(min=2, max=144),
        validators.Regexp('^\w+$',
                          message="Username must contain only letters, numbers or underscore")
    ])
    password = PasswordField("Password", [validators.Length(min=8)])

    class Meta:
        csrf = False


class RegistrationForm(LoginForm):
    """extends LoginForm"""
    name = StringField("Name", [validators.Length(min=2, max=144)])
