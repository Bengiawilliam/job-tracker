from sqlalchemy import Integer, String, Column, Boolean
from .database import Base 

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=False)
    email = Column(String, unique=True, index=False)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)


