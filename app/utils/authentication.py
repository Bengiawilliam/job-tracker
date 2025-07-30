from fastapi import APIRouter, Depends, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from . import hashing
from ..tokens import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['authentication'],
    prefix = "/login"
)

@router.post('/')
def login_dashboard(
    request: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(database.get_db)
):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if user:
        if not hashing.pwd_cxt.verify(request.password, user.password):
            raise HTTPException(status_code=401, detail="Incorrect password")
        
        role = "admin" if user.is_admin else "user"

    else:
        user = db.query(models.Admin).filter(models.Admin.email == request.username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        if not hashing.pwd_cxt.verify(request.password, user.password):
            raise HTTPException(status_code=401, detail="Incorrect password")

        role = "admin"

    access_token = create_access_token(
        data={"sub": user.email, "role": role, "id": user.id}
    )

    return {"access_token": access_token, "token_type": "bearer"}

