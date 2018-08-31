from application import db
from application.models import Base

from sqlalchemy.sql import text


class Question(Base):
    """extends class Base (in application/models)"""
    answer = db.Column(db.String(144), nullable=False)

    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'),
                           nullable=False)

    masteries = db.relationship('Mastery', backref='question', lazy=True)

    def __init__(self, name, answer):
        self.name = name
        self.answer = answer

    @staticmethod
    def find_questions_by_subject_and_masteries_by_account(subject_id, account_id):
        stmt = text("SELECT q.id, q.name, q.answer, m.mastery FROM Question q LEFT JOIN Mastery m"
                    " ON m.question_id = q.id AND m.account_id = :account_id"
                    " WHERE q.subject_id = :subject_id"
                    " ORDER BY m.mastery;").params(subject_id=subject_id, account_id=account_id)

        res = db.engine.execute(stmt)

        return res


class Mastery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mastery = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'),
                            nullable=False)

    def __init__(self, mastery):
        self.mastery = mastery
