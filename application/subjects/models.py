from application import db
from application.models import Base


class Subject(Base):
    """extends class Base (in application/models)"""
    questions = db.relationship("Question", backref='subject', lazy=True)

    def __init__(self, name):
        self.name = name
