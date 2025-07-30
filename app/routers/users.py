from fastapi import APIRouter, Depends, status, HTTPException
from ..utils import hashing
from .. import schemas, database, models
from sqlalchemy.orm import Session
from .. import OAuth2

router = APIRouter(
    prefix="/users",
    tags= ["Users"])


@router.get("/profile")
def get_user_profile(
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(OAuth2.get_current_user)
):
    if current_user.role != "user":
        raise HTTPException(status_code=403, detail="Only users can access this route")
    return {"message": f"Welcome User {current_user.email}"}


@router.get("/",response_model = list[schemas.UserOut])
def get_all_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}", response_model = schemas.ShowUser)
def search_user(id : int,db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user: 
        raise HTTPException(status_code=404, detail="not found")
    return user

@router.post("/job")
def apply_job():
    pass

@router.get("/job/review_status")
def fetch_status():
    pass