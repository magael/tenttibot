from application import db
from application.models import Base

from sqlalchemy.sql import text


class Question(Base):
    """extends class Base (in application/models)"""
    answer = db.Column(db.String(144), nullable=False)
    mastery= db.Column(db.Integer, nullable=False)

    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'),
                           nullable=False)

    def __init__(self, name, answer, mastery):
        self.name = name
        self.answer = answer
        self.mastery = mastery
