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