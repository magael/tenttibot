from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import user_subjects
from application.subjects.models import Subject
from application.subjects.forms import SubjectForm


@app.route("/new/", methods=["GET"])
@login_required
def subjects_form():
    """Page for creating a new subject"""
    return render_template("subjects/new.html", form=SubjectForm())


@app.route("/", methods=["POST"])
@login_required
def subjects_create():
    """Post data to create a new subject"""
    form = SubjectForm(request.form)

    if not form.validate():
        return render_template("index.html")

    s = Subject(form.name.data)

    current_user.subjects.append(s)
    
    db.session.add(s)
    db.session.commit()

    return redirect(url_for("index"))