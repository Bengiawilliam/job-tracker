from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from .database import Base 
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String,index=False)
    password = Column(String)
    full_name = Column(String)
    is_admin = Column(Boolean, default=False)
    blogs = relationship("Blog", back_populates="creator")

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="blogs")

class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, default="John Doe")
    email = Column(String, default='admin@email.com')
    password = Column(String, default = 'adminpass')
    company = Column(String, default="Monaco Tracks .co")
    is_admin = Column(Boolean, default= True)

