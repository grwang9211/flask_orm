from mypy_extensions import TypedDict


class IssueInterface(TypedDict, total=False):
    Issue_id: int
    name: str
    purpose: str
