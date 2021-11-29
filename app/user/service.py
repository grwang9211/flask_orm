from app import db
from typing import List
from .model import User
from .interface import UserInterface

class UserService :
    @staticmethod
    def get_all() -> List[User]:
        return User.query.all()

    @staticmethod
    def get_by_id(id: int) -> User:
        return User.query.get(id)

    @staticmethod
    def update(User: User, User_change_updates: UserInterface) -> User:
        User.update(User_change_updates)
        db.session.commit()
        return User

    @staticmethod
    def delete_by_id(id: int) -> List[int]:
        User = User.query.filter(User.id == id).first()
        if not User:
            return []
        db.session.delete(User)
        db.session.commit()
        return [id]

    @staticmethod
    def create(new_attrs: UserInterface) -> User:
        new_User = User(name=new_attrs["name"], purpose=new_attrs["purpose"])

        db.session.add(new_User)
        db.session.commit()

        return new_User