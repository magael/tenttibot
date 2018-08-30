from application import db
from application.models import Base

from sqlalchemy.sql import text


class Question(Base):
    """extends class Base (in application/models)"""
    answer = db.Column(db.String(144), nullable=False)
    mastery = db.Column(db.Integer, nullable=False)

    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'),
                           nullable=False)

    def __init__(self, name, answer, mastery):
        self.name = name
        self.answer = answer
        self.mastery = mastery

    @staticmethod
    def find_questions_by_subject(subject_id):
        stmt = text("SELECT * FROM Question q"
                    " WHERE q.subject_id = :subject_id"
                    " ORDER BY q.mastery;").params(subject_id=subject_id)

        res = db.engine.execute(stmt)

        return res