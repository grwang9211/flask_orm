from mypy_extensions import TypedDict


class CompanyInterface(TypedDict, total=False):
    id: int 
    name: str 
    phone: str 
    fax: str 
    description: str 
        

    
