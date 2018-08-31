from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.views import current_user_is_admin
from application.auth.models import User
from application.subjects.models import Subject
from application.questions.models import Question, Mastery
from application.questions.forms import QuestionForm


@app.route("/<subject_id>", methods=["GET"])
def questions_index(subject_id):
    """Page for listing questions."""
    s = Subject.query.get(subject_id)
    q = Question.find_questions_by_subject_and_masteries_by_account(subject_id, current_user.get_id())
    a = User.find_author(subject_id)
    admin = current_user_is_admin()
    form = QuestionForm(request.form)
    return render_template("questions/list.html", questions=q, subject_id=subject_id, subject_name=s.name, author=a.first(), admin=admin, form=form)


@app.route("/<subject_id>/new/", methods=["GET"])
@login_required()
def questions_form(subject_id):
    """Page for creating a new question"""
    s = Subject.query.get(subject_id)
    return render_template("questions/new.html", form=QuestionForm(), subject_id=subject_id, subject_name=s.name)


@app.route("/<subject_id>/<question_id>/", methods=["GET"])
@login_required()
def questions_question(subject_id, question_id):
    """Page for question editing"""
    form = QuestionForm(request.form)
    q = Question.query.get(question_id)
    s = Subject.query.get(subject_id)
    return render_template("questions/question.html", form=form, question=q, subject_name=s.name)


@app.route("/<subject_id>/<question_id>/edit/", methods=["POST"])
@login_required()
def questions_edit(subject_id, question_id):
    """Posting data to edit a question"""
    if not is_creator(subject_id) and not current_user_is_admin():
        return login_manager.unauthorized()

    form = QuestionForm(request.form)
    q = Question.query.get(question_id)
    s = Subject.query.get(subject_id)

    if not form.validate():
        return render_template("questions/question.html", form=form, question=q, subject_name=s.name)
    
    q.name = form.name.data
    q.answer = form.answer.data

    m = Mastery.query.filter_by(account_id=current_user.get_id(), question_id=question_id).first()

    if not m:
        ma = Mastery(form.mastery.data)
        ma.account_id = current_user.get_id()
        ma.question_id = question_id
        db.session.add(ma)
    else:
        m.mastery = form.mastery.data

    db.session().commit()

    return redirect(url_for("questions_index", subject_id=subject_id))

@app.route("/<subject_id>/<question_id>/mastery/", methods=["POST"])
@login_required()
def questions_edit_mastery(subject_id, question_id):
    """Posting data to edit a question"""
    form = QuestionForm(request.form)

    # validation
    if not 0 <= form.mastery.data <= 5:
        return redirect(url_for("questions_index", subject_id=subject_id))

    q = Question.query.get(question_id)

    ma = Mastery.query.filter_by(account_id=current_user.get_id(), question_id=question_id).first()
    
    if not ma:
        ma = Mastery(form.mastery.data)
        ma.account_id = current_user.get_id()
        ma.question_id = question_id
        db.session.add(ma)
    else:
        ma.mastery = form.mastery.data

    db.session().commit()

    return redirect(url_for("questions_index", subject_id=subject_id))


@app.route("/<subject_id>/<question_id>/delete/", methods=["POST"])
@login_required()
def questions_delete(subject_id, question_id):
    """Deleting a question"""
    if not is_creator(subject_id) and not current_user_is_admin():
        return login_manager.unauthorized()

    q = Question.query.get(question_id)
    db.session().delete(q)
    db.session().commit()

    return redirect(url_for("questions_index", subject_id=subject_id))


@app.route("/<subject_id>/", methods=["POST"])
@login_required()
def questions_create(subject_id):
    """Post data to create a new question"""
    if not is_creator(subject_id):
        return login_manager.unauthorized()

    form = QuestionForm(request.form)

    q = Question(form.name.data, form.answer.data)

    if not form.validate():
        return render_template("questions/new.html", form=form, subject_id=subject_id, question=q)

    q.subject_id = subject_id

    db.session().add(q)
    db.session().commit()

    # TODO: add initial mastery, like
    # m = Mastery(form.mastery.data)
    # m.account_id = current_user.get_id()
    # m.question_id # isqid
    # m.mastery = form.mastery.data
    # db.session.add(m)
    # but needs q_id

    return redirect(url_for("questions_index", subject_id=subject_id))


def is_creator(subject_id):
    """Prevent users from adding to, editing or deleting material created by another user:"""
    s = Subject.query.get(subject_id)
    if s in current_user.subjects:
        return True
    return False
