from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField

class QuestionForm(FlaskForm):
    name = StringField("Question")
    mastered = BooleanField("Mastered")
 
    class Meta:
        csrf = False