from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email : str
    password : str 
    full_name : str 
    is_active : bool

class UserOut(BaseModel):
    id : int 
    email : str
    fullname: str 

    class Config: 
        orm_mode = True
    

class Admin(BaseModel):
    id: int
    email: str 
    fullname: str

    class Config:
        orm_mode = True


    