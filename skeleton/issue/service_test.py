from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.test.fixtures import app, db  # noqa
from .model import Issue
from .service import IssueService  # noqa
from .interface import IssueInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Issue = Issue(Issue_id=1, name="Yin", purpose="thing 1")
    yang: Issue = Issue(Issue_id=2, name="Yang", purpose="thing 2")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Issue] = IssueService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: Issue = Issue(Issue_id=1, name="Yin", purpose="thing 1")

    db.session.add(yin)
    db.session.commit()
    updates: IssueInterface = dict(name="New Issue name")

    IssueService.update(yin, updates)

    result: Issue = Issue.query.get(yin.Issue_id)
    assert result.name == "New Issue name"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Issue = Issue(Issue_id=1, name="Yin", purpose="thing 1")
    yang: Issue = Issue(Issue_id=2, name="Yang", purpose="thing 2")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    IssueService.delete_by_id(1)
    db.session.commit()

    results: List[Issue] = Issue.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: IssueInterface = dict(name="Fancy new Issue", purpose="Fancy new purpose")
    IssueService.create(yin)
    results: List[Issue] = Issue.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
