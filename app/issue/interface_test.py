from pytest import fixture
from .model import Issue
from .interface import IssueInterface


@fixture
def interface() -> IssueInterface:
    return IssueInterface(Issue_id=1, name="Test Issue", purpose="Test purpose")


def test_IssueInterface_create(interface: IssueInterface):
    assert interface


def test_IssueInterface_works(interface: IssueInterface):
    Issue = Issue(**interface)
    assert Issue
