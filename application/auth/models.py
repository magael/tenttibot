from application import db
from application.models import Base

from sqlalchemy.sql import text


# junction table "UserSubjects"
user_subjects = db.Table('user_subjects',
                         db.Column('account_id', db.Integer, db.ForeignKey(
                             'account.id'), primary_key=True),
                         db.Column('subject_id', db.Integer, db.ForeignKey(
                             'subject.id'), primary_key=True))


class User(Base):
    """extends class Base (in application/models)"""
    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    subjects = db.relationship('Subject', secondary=user_subjects, lazy='subquery',
                               backref=db.backref('users', lazy=True))

    # Sketching how to possibly switch from many-to-many to one-to-many relationship:
    # subjects = db.relationship('Subject', backref='user_subjects', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.admin = False

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if self.admin:
            return ["ADMIN"]
        return ["ANY"]
