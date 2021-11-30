from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app  # noqa
from .service import IssueService
from .schema import IssueSchema
from .model import Issue
from .interface import IssueInterface
from . import BASE_ROUTE


def make_Issue(
    id: int = 123, name: str = "Test Issue", purpose: str = "Test purpose"
) -> Issue:
    return Issue(Issue_id=id, name=name, purpose=purpose)


class TestIssueResource:
    @patch.object(
        IssueService,
        "get_all",
        lambda: [
            make_Issue(123, name="Test Issue 1"),
            make_Issue(456, name="Test Issue 2"),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                IssueSchema(many=True)
                .dump(
                    [
                        make_Issue(123, name="Test Issue 1"),
                        make_Issue(456, name="Test Issue 2"),
                    ]
                )
                
            )
            for r in results:
                assert r in expected

    @patch.object(
        IssueService, "create", lambda create_request: Issue(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(name="Test Issue", purpose="Test purpose")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                IssueSchema()
                .dump(Issue(name=payload["name"], purpose=payload["purpose"]))
                
            )
            assert result == expected


def fake_update(Issue: Issue, changes: IssueInterface) -> Issue:
    # To fake an update, just return a new object
    updated_Issue = Issue(
        Issue_id=Issue.Issue_id, name=changes["name"], purpose=changes["purpose"]
    )
    return updated_Issue


class TestIssueIdResource:
    @patch.object(IssueService, "get_by_id", lambda id: make_Issue(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_Issue(id=123)
            print(f"result = ", result)
            assert result["IssueId"] == expected.Issue_id

    @patch.object(IssueService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected

    @patch.object(IssueService, "get_by_id", lambda id: make_Issue(id=id))
    @patch.object(IssueService, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result = client.put(
                f"/api/{BASE_ROUTE}/123",
                json={"name": "New Issue", "purpose": "New purpose"},
            ).get_json()
            expected = (
                IssueSchema()
                .dump(Issue(Issue_id=123, name="New Issue", purpose="New purpose"))
                
            )
            assert result == expected
