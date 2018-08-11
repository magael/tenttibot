from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.questions.models import Question
from application.questions.forms import QuestionForm

# list questions page
@app.route("/questions", methods=["GET"])
def questions_index():
    return render_template("questions/list.html", questions = Question.query.all())

# new question creation page
@app.route("/questions/new/")
@login_required
def questions_form():
    return render_template("questions/new.html", form = QuestionForm())

# question editing page
@app.route("/questions/<question_id>/", methods=["GET"])
@login_required
def questions_question(question_id):
    form = QuestionForm(request.form)
    q = Question.query.get(question_id)
    return render_template("questions/question.html", form = form, question = q)

# # updating a question's status
# @app.route("/questions/<question_id>/", methods=["POST"]) # better route ...id>/mastered ?
# @login_required
# def questions_set_mastered(question_id):
#     q = Question.query.get(question_id)
#     q.mastered = not q.mastered
#     db.session().commit()
  
#     return redirect(url_for("questions_index"))

# posting data to edit a question
@app.route("/questions/<question_id>/edit/", methods=["POST"])
@login_required
def questions_edit(question_id):
    form = QuestionForm(request.form)
    q = Question.query.get(question_id)

    if not form.validate():
        return render_template("questions/new.html", form = form)

    q.name = form.name.data
    q.mastered = form.mastered.data

    db.session().commit()
  
    return redirect(url_for("questions_index"))

# deleting a question
@app.route("/questions/<question_id>/delete/", methods=["POST"])
@login_required
def questions_delete(question_id):
    q = Question.query.get(question_id)
    db.session().delete(q)
    db.session().commit()

    return redirect(url_for("questions_index"))

# post data to create a new question
@app.route("/questions/", methods=["POST"])
@login_required
def questions_create():
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("questions/new.html", form = form)

    q = Question(form.name.data)
    q.mastered = form.mastered.data
    # TEMP!
    q.subject_id = 1 # CHANGE when subject more developed
    # !

    db.session().add(q)
    db.session().commit()
  
    return redirect(url_for("questions_index"))
    
