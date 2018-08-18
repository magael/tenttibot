from application import db
from application.models import Base


# junction table "UserSubjects"
user_subjects = db.Table('user_subjects',
                 db.Column('subject_id', db.Integer, db.ForeignKey(
                     'subject.id'), primary_key=True),
                 db.Column('account_id', db.Integer, db.ForeignKey(
                     'account.id'), primary_key=True))

# extends class Base (in application/models)
class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    subjects = db.relationship('Subject', secondary=user_subjects, lazy='subquery',
                               backref=db.backref('users', lazy=True))

    # TODO: add roles

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
