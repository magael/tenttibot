from application import app, db
from flask import redirect, render_template, request, url_for
from application.questions.models import Question
from application.questions.forms import QuestionForm

@app.route("/questions", methods=["GET"])
def questions_index():
    return render_template("questions/list.html", questions = Question.query.all())

@app.route("/questions/new/")
def questions_form():
    return render_template("questions/new.html", form = QuestionForm())

@app.route("/questions/<question_id>/", methods=["POST"])
def questions_set_mastered(question_id):

    q = Question.query.get(question_id)
    q.mastered = True # can't change back again. better: mastered = !mastered?
    db.session().commit()
  
    return redirect(url_for("questions_index"))

@app.route("/questions/", methods=["POST"])
def questions_create():
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("questions/new.html", form = form)

    q = Question(form.name.data)
    q.mastered = form.mastered.data

    db.session().add(q)
    db.session().commit()
  
    return redirect(url_for("questions_index"))