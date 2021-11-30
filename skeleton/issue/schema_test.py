from pytest import fixture

from .model import Issue
from .schema import IssueSchema
from .interface import IssueInterface


@fixture
def schema() -> IssueSchema:
    return IssueSchema()


def test_IssueSchema_create(schema: IssueSchema):
    assert schema


def test_IssueSchema_works(schema: IssueSchema):
    params: IssueInterface = schema.load(
        {"IssueId": "123", "name": "Test Issue", "description": "This is a test issue", "purpose": "Test purpose"}
    )
    Issue = Issue(**params)

    assert Issue.Issue_id == 123
    assert Issue.name == "Test Issue"
    assert Issue.description == "This is a test issue"
    assert Issue.purpose == "Test purpose"
