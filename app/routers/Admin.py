from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get('/')
def root():
    return {"nothing"}

@router.get('/management/')
def viewAll(db: Session = Depends(database.get_db)):
    all_data = db.query(models.User).all()  
    return all_data

@router.delete('/management/{user_id}', status_code=status.HTTP_404_NOT_FOUND)
def delete(user_id : int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {f"successfully deleted the user {user_id}"}

@router.patch('/management/{user_id}', status_code=status.HTTP_304_NOT_MODIFIED)
def update(user_id: int, request : schemas.UserUpdate, db: Session = Depends(database.get_db)): 
    user = db.query(models.User).filter(models.User.id == user_id).first()
    user.email = request.email
    user.full_name = request.full_name 
    db.commit()
    db.refresh(user)
    return user    
