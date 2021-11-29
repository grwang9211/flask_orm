from app import db
from typing import List
from .model import Company
from .interface import CompanyInterface

class CompanyService :
    @staticmethod
    def get_all() -> List[Company]:
        return Company.query.all()

    @staticmethod
    def get_by_id(id: int) -> Company:
        return Company.query.get(id)

    @staticmethod
    def update(Company: Company, Company_change_updates: CompanyInterface) -> Company:
        Company.update(Company_change_updates)
        db.session.commit()
        return Company

    @staticmethod
    def delete_by_id(id: int) -> List[int]:
        Company = Company.query.filter(Company.id == id).first()
        if not Company:
            return []
        db.session.delete(Company)
        db.session.commit()
        return [id]

    @staticmethod
    def create(new_attrs: CompanyInterface) -> Company:
        new_Company = Company(name=new_attrs["name"], purpose=new_attrs["purpose"])

        db.session.add(new_Company)
        db.session.commit()

        return new_Company