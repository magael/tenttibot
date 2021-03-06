from application import db
from application import db
from application.models import Base

from sqlalchemy.sql import text


class Subject(Base):
    """extends class Base (in application/models)"""
    questions = db.relationship("Question", backref='subject', lazy=True)
    
    def __init__(self, name):
        self.name = name


    @staticmethod
    def subjects_with_question_counts():
        """Subjects with the same name are listed separately."""
        """Ordered by most recent subject."""
        stmt = text("SELECT s.id, s.name, COUNT(q.id) FROM Subject s"
                    " LEFT JOIN Question q ON q.subject_id = s.id"
                    " GROUP BY s.id ORDER BY s.date_created DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1], "questions": row[2]})

        return response
