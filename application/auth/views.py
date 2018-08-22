from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, login_required
from application.auth.models import User, Role
from application.auth.forms import LoginForm, RegistrationForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout", methods=["GET"])
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/register.html", form=RegistrationForm())

    form = RegistrationForm(request.form)

    taken = User.query.filter_by(username=form.username.data)
    if taken.first():
        taken_error = ("Sorry, the username has already been taken!")
    else:
        taken_error = False

    if not form.validate() or taken_error:
        return render_template("auth/register.html", form = form, taken=taken_error)

    u = User(form.name.data, form.username.data, form.password.data)

    # TODO: if the role "ANY" exists, append that rather than creating a new role
    r = Role("ANY")
    u.auth_roles.append(r)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/accounts", methods=["GET"])
@login_required(role="ADMIN")
def users_index():
    #BUG: Heroku gives always 500: Internal server error (works locally)
    return render_template("auth/list.html", accounts = User.users_and_roles())