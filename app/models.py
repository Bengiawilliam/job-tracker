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
    companies = relationship("Company", back_populates="employee")

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="blogs")

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True)
    name =  Column(String, default = "Monaco Tracks.co")
    motto = Column(String, default = "Innovation in you!!")
    user_id = Column(Integer, ForeignKey('users.id'))
    position = Column(String, default="Recruiter")
    jobs = relationship("Job", back_populates="companies")
    employee = relationship("User", back_populates="companies")

class Job(Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, default = "SDE Intern")
    description = Column(String, default = "Looking for a good student with talents")
    Company_id = Column(Integer, ForeignKey('company.id'))
    companies = relationship("Company", back_populates="jobs")
    
class JobApplications(Base):
    __tablename__ = "jobapplications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    company_name = Column(String, ForeignKey('company.name'))
    position = Column(String)
    status = Column(String)
    user_name = Column(String, ForeignKey('users.full_name'))
    
    




