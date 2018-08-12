from application import db
from application.models import Base

from sqlalchemy.sql import text


class Question(Base):
    """extends class Base (in application/models)"""
    mastered = db.Column(db.Boolean, nullable=False)

    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.mastered = False

    @staticmethod
    def find_questions_by_subject(subject_id):
        # TODO:
        stmt = text("SELECT Question.id, Question.name, Question.mastered FROM Question"
                    " LEFT JOIN Subject on Subject.id = Question.subject_id"
                    " GROUP BY Question.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "mastered":row[2]})

        return response
