from mypy_extensions import TypedDict


class UserInterface(TypedDict, total=False):
    id: int 
    email: str 
    firstname: str 
    lastname: str 
    phone: str 
    company_id: int 
        

    
