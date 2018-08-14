from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.questions.models import Question
from application.questions.forms import QuestionForm


# TODO: change all "questions" routes to "<subject_id>"

@app.route("/<subject_id>", methods=["GET"])
def questions_index(subject_id):
    """Page for listing questions."""
    return render_template("questions/list.html", questions=Question.query.filter_by(subject_id=subject_id), subject_id=subject_id)


@app.route("/<subject_id>/new/")
@login_required
def questions_form(subject_id):
    """Page for creating a new question"""
    return render_template("questions/new.html", form=QuestionForm(), subject_id=subject_id)


@app.route("/<subject_id>/<question_id>/", methods=["GET"])
@login_required
def questions_question(subject_id, question_id):
    """Page for question editing"""
    form = QuestionForm(request.form)
    q = Question.query.get(question_id)
    return render_template("questions/question.html", form=form, question=q)

@app.route("/<subject_id>/<question_id>/edit/", methods=["POST"])
@login_required
def questions_edit(subject_id, question_id):
    """Posting data to edit a question"""
    form = QuestionForm(request.form)
    q = Question.query.get(question_id)

    if not form.validate():
        return redirect(url_for("questions_index", subject_id=subject_id))

    q.name = form.name.data
    q.mastered = form.mastered.data

    db.session().commit()

    return redirect(url_for("questions_index", subject_id=subject_id))


@app.route("/<subject_id>/<question_id>/delete/", methods=["POST"])
@login_required
def questions_delete(subject_id, question_id):
    """Deleting a question"""
    q = Question.query.get(question_id)
    db.session().delete(q)
    db.session().commit()

    return redirect(url_for("questions_index", subject_id=subject_id))


@app.route("/<subject_id>/", methods=["POST"])
@login_required
def questions_create(subject_id):
    """Post data to create a new question"""
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("questions/new.html", form=form, subject_id=subject_id)

    q = Question(form.name.data)
    q.mastered = form.mastered.data
    q.subject_id = subject_id

    db.session().add(q)
    db.session().commit()

    return redirect(url_for("questions_index", subject_id=subject_id))
