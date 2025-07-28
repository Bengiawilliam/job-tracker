from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models
from .. import utils, OAuth2


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/admin/data")
def get_admin_data(db: Session = Depends(database.get_db),current_admin: schemas.TokenData = Depends(OAuth2.get_current_user)):
    if current_admin.role != 'admin':
        return {"unauthorized access"}
    return {"message": f"Welcome Admin {current_admin.email}"}

@router.get('/management/')
def viewAll(db: Session = Depends(database.get_db), get_current_user : schemas.Admin = Depends(OAuth2.get_current_user)):
    if get_current_user.role != "admin":
        return {"unauthorized access"}
    all_data = db.query(models.User).all()  
    return all_data

@router.delete('/management/{user_id}')
def delete(user_id : int, db: Session = Depends(database.get_db),get_current_user : schemas.Admin = Depends(OAuth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {f"successfully deleted the user {user_id}"}

@router.patch('/management/{user_id}')
def update(user_id: int, request : schemas.UserUpdate, db: Session = Depends(database.get_db), get_current_user : schemas.Admin = Depends(OAuth2.get_current_user)): 
    user = db.query(models.User).filter(models.User.id == user_id).first()
    user.email = request.email
    user.full_name = request.full_name 
    db.commit()
    db.refresh(user)
    return user    

@router.post('/create/')
def create_admin(request : schemas.createAdmin, db:Session = Depends(database.get_db)):
    hashed_password = utils.hashing.pwd_cxt.hash(request.password)
    admin = models.Admin(
        full_name = request.username,
        email = request.email,
        password = hashed_password,
        company = request.company,
        is_admin = True
        )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin 

