from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email : EmailStr
    password : str 
    fullname : str 

class UserOut(BaseModel):
    id : int 
    email : EmailStr
    fullname: str 

    class Config: 
        orm_mode = True
        

    