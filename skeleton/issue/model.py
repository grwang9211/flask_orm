from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import IssueInterface


class Issue(db.Model):  # type: ignore
    """A snazzy Issue"""

    __tablename__ = "Issue"

    Issue_id = Column(Integer(), primary_key=True)
    description = Column(String(4096))
    name = Column(String(255))
    purpose = Column(String(255))

    def update(self, changes: IssueInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
