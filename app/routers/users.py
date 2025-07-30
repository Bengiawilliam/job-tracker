from fastapi import APIRouter, Depends, status, HTTPException
from ..utils import hashing
from .. import schemas, database, models
from sqlalchemy.orm import Session
from .. import OAuth2

router = APIRouter(
    prefix="/users",
    tags= ["Users"])


@router.get("/login")
def login(
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(OAuth2.get_current_user)
):
    if current_user.role != "user":
        raise HTTPException(status_code=403, detail="Only users can access this route")
    return {"message": f"Welcome User {current_user.email}"}


@router.get("/search/all_user",response_model = list[schemas.UserOut])
def get_all_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/search/preview_user/{id}", response_model = schemas.ShowUser)
def search_user(id : int,db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user: 
        raise HTTPException(status_code=404, detail="not found")
    return user

@router.get('/search/company', response_model=list[schemas.CompanyOut])
def view_all_companies(db: Session = Depends(database.get_db)):
    companies = db.query(models.Company).all()
    return companies

@router.post("/search/job")
def search_jobs():
    pass 

@router.post("/jobs/apply")
def apply_job():
    pass

@router.get("/jobs/review_status")
def fetch_status():
    pass

