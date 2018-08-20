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

    db.session.add(s)
    db.session.commit()
    
    # I hope using the "engine.execute()" is fine since it's not inserting any user input.
    db.engine.execute(user_subjects.insert(), account_id=current_user.id, subject_id=s.id)
    db.session.commit() # seems to work without this as well

    return redirect(url_for("index"))