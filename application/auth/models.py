from application import db
from application.models import Base

from sqlalchemy.sql import text


user_subjects = db.Table('user_subjects',
                         db.Column('account_id', db.Integer, db.ForeignKey(
                             'account.id'), primary_key=True),
                         db.Column('subject_id', db.Integer, db.ForeignKey(
                             'subject.id'), primary_key=True))

user_roles = db.Table('user_roles',
                      db.Column('account_id', db.Integer, db.ForeignKey(
                          'account.id'), primary_key=True),
                      db.Column('role_id', db.Integer, db.ForeignKey(
                          'role.id'), primary_key=True))


class User(Base):
    """extends class Base (in application/models)"""
    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    masteries = db.relationship('Mastery', backref='user', lazy=True)

    subjects = db.relationship('Subject', secondary=user_subjects, lazy='subquery',
                               backref=db.backref('users', lazy=True))
    auth_roles = db.relationship('Role', secondary=user_roles, lazy='subquery',
                                 backref=db.backref('users', lazy=True))

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

    def roles(self):
        return self.auth_roles

    @staticmethod
    def users_and_roles():
        stmt = text("SELECT a.id, a.username, r.name FROM account a"
                    " LEFT JOIN Role r"
                    " ON a.id IN (SELECT account_id FROM user_roles ur"
                    " WHERE ur.account_id = a.id AND ur.role_id = r.id)"
                    " GROUP BY a.id, r.name ORDER BY r.name, a.username;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(
                {"user_id": row[0], "username": row[1], "role": row[2]})

        return response

    @staticmethod
    def find_author(subject_id):
        # TODO: The following would not work correctly with many users per subject
        # Consider switching user_subjects to many-to-one
        # Or add date_created & -modified to user_subjects and order this query by us.date_created
        stmt = text("SELECT * FROM account a"
                    " LEFT JOIN user_subjects us"
                    " ON us.subject_id = :subject_id"
                    " WHERE a.id = us.account_id;").params(subject_id=subject_id)
        res = db.engine.execute(stmt)

        return res


class Role(Base):
    """extends class Base (in application/models)"""

    def __init__(self, name):
        self.name = name
