from .model import Issue  # noqa
from .schema import IssueSchema  # noqa

BASE_ROUTE = "Issue"


def register_routes(api, app, root="api"):
    from .controller import api as Issue_api

    api.add_namespace(Issue_api, path=f"/{root}/{BASE_ROUTE}")
