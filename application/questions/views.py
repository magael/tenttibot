from application import app, db
from flask import redirect, render_template, request, url_for
from application.questions.models import Question

@app.route("/questions", methods=["GET"])
def questions_index():
    return render_template("questions/list.html", questions = Question.query.all())

@app.route("/questions/new/")
def questions_form():
    return render_template("questions/new.html")

@app.route("/questions/<question_id>/", methods=["POST"])
def questions_set_mastered(question_id):

    t = Question.query.get(question_id)
    t.mastered = True
    db.session().commit()
  
    return redirect(url_for("questions_index"))

@app.route("/questions/", methods=["POST"])
def questions_create():
    t = Question(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("questions_index"))