from pydantic import BaseModel, EmailStr
from typing import Optional

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

class UserUpdate(BaseModel):
    fullname : Optional[str] = None
    email : Optional[str] = None
    