from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class QuestionForm(FlaskForm):
    name = StringField("Question", [validators.Length(min=1, max=144)])
    answer = StringField("Answer", [validators.Length(min=1, max=144)])
    mastery = IntegerField("Mastery", [validators.NumberRange(min=0, max=5)], default=0)
 
    class Meta:
        csrf = False