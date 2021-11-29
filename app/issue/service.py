from app import db
from typing import List
from .model import Issue
from .interface import IssueInterface


class IssueService:
    @staticmethod
    def get_all() -> List[Issue]:
        return Issue.query.all()

    @staticmethod
    def get_by_id(Issue_id: int) -> Issue:
        return Issue.query.get(Issue_id)

    @staticmethod
    def update(Issue: Issue, Issue_change_updates: IssueInterface) -> Issue:
        Issue.update(Issue_change_updates)
        db.session.commit()
        return Issue

    @staticmethod
    def delete_by_id(Issue_id: int) -> List[int]:
        Issue = Issue.query.filter(Issue.Issue_id == Issue_id).first()
        if not Issue:
            return []
        db.session.delete(Issue)
        db.session.commit()
        return [Issue_id]

    @staticmethod
    def create(new_attrs: IssueInterface) -> Issue:
        new_Issue = Issue(name=new_attrs["name"], purpose=new_attrs["purpose"])

        db.session.add(new_Issue)
        db.session.commit()

        return new_Issue
