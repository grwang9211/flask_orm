from sqlalchemy import Integer, Column, String, ForeignKey
from app import db  # noqa
from .interface import UserInterface


class User(db.Model):  # type: ignore

    """User"""
    
    __tablename__ = "user"

    id = Column( Integer() , primary_key=True )
    email = Column( String(255)  )
    firstname = Column( String(255)  )
    lastname = Column( String(255)  )
    phone = Column( String(16)  )
    company_id = Column( Integer() , ForeignKey('company.id') )
    

    def update(self, changes: UserInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self