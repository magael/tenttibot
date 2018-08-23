from application import db
from application import db
from application.models import Base

from sqlalchemy.sql import text


class Subject(Base):
    """extends class Base (in application/models)"""
    questions = db.relationship("Question", backref='subject', lazy=True)
    # Sketching how to possibly switch from many-to-many to one-to-many relationship:
    # account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
    #                        nullable=False)
    
    def __init__(self, name):
        self.name = name


    # TODO: list separately "My subjects" and 10 most recent "Other user's subjects"
    @staticmethod
    def subjects_with_question_counts():
        """Subjects with the same name are listed separately."""
        """Ordered by most recent subject."""
        # IDEA: Add avg mastery of questions in each subject
        # IDEA: Order the results by q.date_modified DESC
        stmt = text("SELECT s.id, s.name, COUNT(q.id) FROM Subject s"
                    " LEFT JOIN Question q ON q.subject_id = s.id"
                    " GROUP BY s.id ORDER BY s.date_created DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1], "questions": row[2]})

        return response
