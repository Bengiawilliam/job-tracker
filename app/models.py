from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, func, DateTime
from .database import Base 
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String,index=False)
    password = Column(String)
    full_name = Column(String)
    is_admin = Column(Boolean, default=False)
    company_id = Column(Integer, ForeignKey("company.id"), nullable=True)
    blogs = relationship("Blog", back_populates="creator")
    companies = relationship("Company", back_populates="employee")
    applications = relationship("JobApplications", back_populates="user")

class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String,index=False)
    password = Column(String)
    full_name = Column(String)
    is_admin = Column(Boolean, default=False)
    companies = relationship("Company", back_populates="admin")



class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True)
    name =  Column(String, default = "Monaco Tracks.co")
    motto = Column(String, default = "Innovation in you!!")
    admin_id = Column(Integer, ForeignKey("admin.id"), unique=True)
    jobs = relationship("Job", back_populates="companies")
    employee = relationship("User", back_populates="companies")
    applications = relationship("JobApplications", back_populates="companies")
    admin = relationship("Admin", back_populates="companies")

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="blogs")

class Job(Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, default = "SDE Intern")
    description = Column(String, default = "Looking for a good student with talents")
    position = Column(String)
    company_id = Column(Integer, ForeignKey('company.id'))
    companies = relationship("Company", back_populates="jobs")
    applications = relationship("JobApplications", back_populates="jobs")

class JobApplications(Base):
    __tablename__ = "jobapplications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    company_name = Column(String, ForeignKey('company.name'))
    position = Column(String, ForeignKey("job.position"))
    status = Column(String)
    resume_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user = relationship("User", back_populates="applications")
    companies = relationship("Company", back_populates="applications")
    jobs = relationship("Job", back_populates="applications")


    




