from flask import render_template
from application import app
from application.subjects.models import Subject

@app.route("/")
def index():
    return render_template("index.html", subjects = Subject.subjects_with_question_counts())