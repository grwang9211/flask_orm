from .model import Company  # noqa
from .schema import CompanySchema  # noqa

BASE_ROUTE = "Company"


def register_routes(api, app, root="api"):
    from .controller import api as Company_api

    api.add_namespace(Company_api, path=f"/{root}/{BASE_ROUTE}")