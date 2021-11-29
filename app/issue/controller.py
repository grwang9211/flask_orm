from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import IssueSchema
from .service import IssueService
from .model import Issue
from .interface import IssueInterface

api = Namespace("Issue", description="Single namespace, single entity")  # noqa


@api.route("/")
class IssueResource(Resource):
    """Issues"""

    @responds(schema=IssueSchema, many=True)
    def get(self) -> List[Issue]:
        """Get all Issues"""

        return IssueService.get_all()

    @accepts(schema=IssueSchema, api=api)
    @responds(schema=IssueSchema)
    def post(self) -> Issue:
        """Create a Single Issue"""

        return IssueService.create(request.parsed_obj)


@api.route("/<int:IssueId>")
@api.param("IssueId", "Issue database ID")
class IssueIdResource(Resource):
    @responds(schema=IssueSchema)
    def get(self, IssueId: int) -> Issue:
        """Get Single Issue"""

        return IssueService.get_by_id(IssueId)

    def delete(self, IssueId: int) -> Response:
        """Delete Single Issue"""
        from flask import jsonify

        id = IssueService.delete_by_id(IssueId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=IssueSchema, api=api)
    @responds(schema=IssueSchema)
    def put(self, IssueId: int) -> Issue:
        """Update Single Issue"""

        changes: IssueInterface = request.parsed_obj
        Issue = IssueService.get_by_id(IssueId)
        return IssueService.update(Issue, changes)
