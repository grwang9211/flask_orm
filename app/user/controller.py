from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import UserSchema
from .service import UserService
from .model import User
from .interface import UserInterface

api = Namespace("User", description="Single namespace, single entity")  # noqa


@api.route("/")
class UserResource(Resource):
    """Users"""

    @responds(schema=UserSchema, many=True)
    def get(self) -> List[User]:
        """Get all Users"""

        return UserService.get_all()

    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema)
    def post(self) -> User:
        """Create a Single User"""

        return UserService.create(request.parsed_obj)


@api.route("/<int:Id>")
@api.param("Id", "User database ID")
class IdResource(Resource):
    @responds(schema=UserSchema)
    def get(self, Id: int) -> User:
        """Get Single User"""

        return UserService.get_by_id(Id)

    def delete(self, Id: int) -> Response:
        """Delete Single User"""
        from flask import jsonify

        id = UserService.delete_by_id(Id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema)
    def put(self, Id: int) -> User:
        """Update Single User"""

        changes: UserInterface = request.parsed_obj
        User = UserService.get_by_id(Id)
        return UserService.update(User, changes)