from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


# TODO: Base class AuthForm?


class LoginForm(FlaskForm):
    # ok not to validate since it's done in registration, right?
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class RegistrationForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=144)])
    username = StringField("Username", [
        validators.Length(min=2, max=144),
        validators.Regexp('^\w+$',
                          message="Username must contain only letters, numbers or underscore")
    ])
    password = PasswordField("Password", [validators.Length(min=8)])

    class Meta:
        csrf = False
