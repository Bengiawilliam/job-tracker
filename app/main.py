from fastapi import FastAPI
from .routers import users, Admin
from . import models, database


app = FastAPI() 

models.Base.metadata.create_all(database.engine)

app.include_router(users.router)
app.include_router(Admin.router)

