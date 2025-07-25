from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from .database import Base 
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=False)
    password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    blogs = relationship("Blog", back_populates="creator")

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="blogs")