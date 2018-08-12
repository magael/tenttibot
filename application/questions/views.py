from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.questions.models import Question
from application.questions.forms import QuestionForm


@app.route("/questions", methods=["GET"])
def questions_index():
    """Page for isting questions."""
    # BUG: looks like it displays all questions, not only those with the correct subject_id
    # (same questions displayed when changing the url "...?subject_id=" value "1" to any other number)
    # TODO: try questions = Question.query.filter_by(...
    s = request.args.get('subject_id')
    return render_template("questions/list.html", questions=Question.find_questions_by_subject(s))
    # return render_template("questions/list.html", questions=Question.query.all())


@app.route("/questions/new/")
@login_required
def questions_form():
    """Page for creating a new question"""
    return render_template("questions/new.html", form=QuestionForm())


@app.route("/questions/<question_id>/", methods=["GET"])
@login_required
def questions_question(question_id):
    """Page for question editing"""
    form = QuestionForm(request.form)
    q = Question.query.get(question_id)
    return render_template("questions/question.html", form=form, question=q)

# # updating a question's status
# @app.route("/questions/<question_id>/", methods=["POST"]) # IDEA: better route ...id>/mastered ?
# @login_required
# def questions_set_mastered(question_id):
#     q = Question.query.get(question_id)
#     q.mastered = not q.mastered
#     db.session().commit()

#     return redirect(url_for("questions_index"))


@app.route("/questions/<question_id>/edit/", methods=["POST"])
@login_required
def questions_edit(question_id):
    """Posting data to edit a question"""
    form = QuestionForm(request.form)
    q = Question.query.get(question_id)

    if not form.validate():
        return render_template("questions/new.html", form=form)

    q.name = form.name.data
    q.mastered = form.mastered.data

    s = q.subject_id

    db.session().commit()

    return redirect(url_for("questions_index", subject_id=s))


@app.route("/questions/<question_id>/delete/", methods=["POST"])
@login_required
def questions_delete(question_id):
    """Deleting a question"""
    q = Question.query.get(question_id)
    s = q.subject_id
    db.session().delete(q)
    db.session().commit()

    return redirect(url_for("questions_index", subject_id=s))


@app.route("/questions/", methods=["POST"])
@login_required
def questions_create():
    """Post data to create a new question"""
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("questions/new.html", form=form)

    q = Question(form.name.data)
    q.mastered = form.mastered.data
    # HACK
    q.subject_id = 1  # TODO: get actual current subject id when subject more developed

    s = q.subject_id

    db.session().add(q)
    db.session().commit()

    return redirect(url_for("questions_index", subject_id=s))
