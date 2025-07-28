from pydantic import BaseModel, EmailStr
from typing import Optional, List

class User(BaseModel):
    email : str
    password : str 
    full_name : str 
    is_admin : bool

class Blog(BaseModel):
    title : str 
    body : str
    class Config: 
        orm_mode = True

class UserOut(BaseModel):
    id : int 
    email : str
    full_name: str 

    class Config: 
        orm_mode = True
    

class Admin(BaseModel):
    id: int
    email: str 
    full_name: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    full_name : Optional[str] = None
    email : Optional[str] = None

class BlogCreate(BaseModel):
    title : str 
    body : str
    user_id : int

class ShowBlog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    id : int
    full_name : str 
    email : str 
    blogs: List[Blog]  = [] 
    class Config:
        orm_mode = True

class Login(BaseModel):
    username : str 
    password : str 

class Token(BaseModel):
    access_token: str
    token_type: str




class TokenData(BaseModel):
    email: Optional[str] = None
    role: str

class createAdmin(BaseModel):
    username : str 
    email : str 
    password : str 
    company : str 
    is_admin : bool 




    