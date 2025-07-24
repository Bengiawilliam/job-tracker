from fastapi import APIRouter, Depends, HTTPException
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

@router.delete('/management/{user_id}')
def delete(user_id : int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        assert HTTPException(status_code=404, detail="file not found")
    db.delete(user)
    db.commit()
    return {f"successfully deleted the user {user_id}"}

@router.patch('/management/{user_id}')
def update(user_id: int, request : schemas.UserUpdate, db: Session = Depends(database.get_db)): 
    user = db.query(models.User).filter(models.User.id == user_id).first()
    
    if user is None: 
        raise HTTPException(status_code=404, detail="user not found")
    
    if request.email is not None: 
        user.email = request.email

    if request.fullname is not None:
        user.full_name = request.fullname 

    db.commit()
    db.refresh(user)
    return user    
#