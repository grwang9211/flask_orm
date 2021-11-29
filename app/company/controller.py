from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import CompanySchema
from .service import CompanyService
from .model import Company
from .interface import CompanyInterface

api = Namespace("Company", description="Single namespace, single entity")  # noqa


@api.route("/")
class CompanyResource(Resource):
    """Companys"""

    @responds(schema=CompanySchema, many=True)
    def get(self) -> List[Company]:
        """Get all Companys"""

        return CompanyService.get_all()

    @accepts(schema=CompanySchema, api=api)
    @responds(schema=CompanySchema)
    def post(self) -> Company:
        """Create a Single Company"""

        return CompanyService.create(request.parsed_obj)


@api.route("/<int:Id>")
@api.param("Id", "Company database ID")
class IdResource(Resource):
    @responds(schema=CompanySchema)
    def get(self, Id: int) -> Company:
        """Get Single Company"""

        return CompanyService.get_by_id(Id)

    def delete(self, Id: int) -> Response:
        """Delete Single Company"""
        from flask import jsonify

        id = CompanyService.delete_by_id(Id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=CompanySchema, api=api)
    @responds(schema=CompanySchema)
    def put(self, Id: int) -> Company:
        """Update Single Company"""

        changes: CompanyInterface = request.parsed_obj
        Company = CompanyService.get_by_id(Id)
        return CompanyService.update(Company, changes)