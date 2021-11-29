from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import CompanyInterface


class Company(db.Model):  # type: ignore

    """Company"""
    
    __tablename__ = "company"

    id = Column( Integer() , primary_key=True )
    name = Column( String(32)  )
    phone = Column( String(16)  )
    fax = Column( String(16)  )
    description = Column( String(255)  )
    

    def update(self, changes: CompanyInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self