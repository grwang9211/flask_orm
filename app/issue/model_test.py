from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from app.test.fixtures import app, db  # noqa
from .model import Issue


@fixture
def Issue() -> Issue:
    return Issue(Issue_id=1, name="Test Issue", description="this is a test issue", purpose="Test purpose")


def test_Issue_create(Issue: Issue):
    assert Issue


def test_Issue_retrieve(Issue: Issue, db: SQLAlchemy):  # noqa
    db.session.add(Issue)
    db.session.commit()
    s = Issue.query.first()
    assert s.__dict__ == Issue.__dict__
