from fastapi import FastAPI
from .routers import users, Admin, blogs
from . import models, database
from .utils import authentication


app = FastAPI() 

#models.Base.metadata.drop_all(bind=database.engine)
models.Base.metadata.create_all(bind=database.engine)

app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(Admin.router)
app.include_router(blogs.router)

