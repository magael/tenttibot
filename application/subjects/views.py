from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db, login_manager, login_required
from application.auth.models import user_subjects
from application.subjects.forms import SubjectForm
from application.subjects.models import Subject
from application.questions.models import Question
from application.questions.views import is_creator


@app.route("/new/", methods=["GET"])
@login_required()
def subjects_form():
    """Page for creating a new subject"""
    return render_template("subjects/new.html", form=SubjectForm())


@app.route("/", methods=["POST"])
@login_required()
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

@app.route("/<subject_id>/edit/", methods=["GET"])
@login_required()
def subjects_subject(subject_id):
    """Page for subject editing"""
    form = SubjectForm(request.form)
    s = Subject.query.get(subject_id)
    return render_template("subjects/subject.html", form=form, subject=s)

@app.route("/<subject_id>/edit/", methods=["POST"])
@login_required()
def subjects_edit(subject_id):
    """Posting data to edit a subject"""
    if not is_creator(subject_id):
        return login_manager.unauthorized()

    form = SubjectForm(request.form)
    s = Subject.query.get(subject_id)

    if not form.validate():
        return render_template("subjects/subject.html", form=form, subject=s)

    s.name = form.name.data

    db.session().commit()

    return redirect(url_for("questions_index", subject_id=subject_id))

@app.route("/<subject_id>/delete/", methods=["POST"])
@login_required()
def subjects_delete(subject_id):
    """Deleting a subject and all it's questions"""
    if not is_creator(subject_id):
        return login_manager.unauthorized()

    s = Subject.query.get(subject_id)
    questions = Question.query.filter_by(subject_id=subject_id)

    for q in questions:
        db.session().delete(q)
    db.session().delete(s)
    db.session().commit()

    return redirect(url_for("index"))