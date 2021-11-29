from .model import User  # noqa
from .schema import UserSchema  # noqa

BASE_ROUTE = "User"


def register_routes(api, app, root="api"):
    from .controller import api as User_api

    api.add_namespace(User_api, path=f"/{root}/{BASE_ROUTE}")