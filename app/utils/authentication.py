from fastapi import APIRouter, Depends, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from . import hashing
from ..token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(request : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="invalid credentials")
    
    if not hashing.pwd_cxt.verify(request.password,user.password):
        raise HTTPException(status_code=404, detail="incorrect password")

    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token":access_token, "token_type":"bearer"}