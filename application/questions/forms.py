from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class QuestionForm(FlaskForm):
    name = StringField("Question", [validators.Length(min=1, max=144, message = 'Field must be between 1 and 144 characters long. Go backwards one page with your browser to restore the content.')])
    answer = StringField("Answer", [validators.Length(min=1, max=144, message = 'Field must be between 1 and 144 characters long. Go backwards one page with your browser to restore the content.')])
    mastery = IntegerField("Mastery", [validators.NumberRange(min=0, max=5)])
 
    class Meta:
        csrf = False