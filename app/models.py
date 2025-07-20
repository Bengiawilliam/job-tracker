from sqlalchemy import Integer, String, Column, Boolean
from .database import Base 

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=False)
    password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)

#class Admin(Base):
