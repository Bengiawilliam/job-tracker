from pydantic import BaseModel, EmailStr
from typing import Optional, List

class User(BaseModel):
    email : Optional[str] = "abc@gmail.com"
    password : Optional[str] = "password"
    full_name : Optional[str] = "Jane Doe"
    resume : Optional[str] = "my_resume.cloud.in"

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
    id : int

class createAdmin(BaseModel):
    name : Optional[str] = "Stalin"
    email : Optional[str] = "stalker@work.in"
    password : Optional[str] = "password"
    company : Optional[str] = "Monaco Tracks.co"



class Company(BaseModel):
    name: Optional[str] = "Monaco Tracks.co"
    motto: Optional[str] = "Innovation in you!!"


class AdminOut(BaseModel):
    name : str 
    email : str
    company : str  

    class Config:
        orm_mode = True

class JobPost(BaseModel):
    position : Optional[str] = "SDE"
    description : Optional[str] = "knowledge of FastAPI is a plus also deep learning models"
    title : Optional[str] = "Seeking for young talents"

class CreateCompany(BaseModel):
    name : Optional[str] = ""
    motto : str
    
class CompanyOut(BaseModel):
    name : str
    motto : str 

    class Config:
        orm_mode = True 
