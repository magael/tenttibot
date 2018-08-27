from flask import render_template
from flask_login import current_user

from application import app
from application.auth.models import User
from application.subjects.models import Subject

@app.route("/")
def index():
    admin = is_admin(current_user.get_id())

    return render_template("index.html", subjects = Subject.subjects_with_question_counts(), admin=admin)

def is_admin(user_id):
    roles = User.users_and_roles()
    for r in roles:
        if r['user_id'] == user_id and r['role'] == "ADMIN":
            return True
    return False