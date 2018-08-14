from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class QuestionForm(FlaskForm):
    name = StringField("Question", [validators.Length(min=2, max=144)])
    mastered = BooleanField("Mastered")
 
    class Meta:
        csrf = False