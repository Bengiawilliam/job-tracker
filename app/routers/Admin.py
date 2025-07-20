from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session
from .. import schemas, database, models

router = APIRouter(
    prefix="/admin"
)

@router.get('/')
def root():
    return {"nothing"}

@router.get('/management/')
def viewAll(db: Session = Depends(database.get_db)):
    all_data = db.query(models.User).all()  
    return all_data



        