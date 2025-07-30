from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models
from .. import utils, OAuth2


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/profile", response_model= schemas.AdminOut)
def get_admin_data(db: Session = Depends(database.get_db),current_admin: schemas.TokenData = Depends(OAuth2.get_current_user)):
    if current_admin.role != 'admin':
        raise HTTPException(status_code=401, detail="unauthorized access")
    admin_data = db.query(models.Admin).filter(models.Admin.id == current_admin.id).first()
    company = db.query(models.Company).filter(models.Company.admin_id== current_admin.id).first()

    if not admin_data or not company:
        raise HTTPException(status_code=404, detail="file not found")
    
    return schemas.AdminOut(
        name=admin_data.full_name,
        email=admin_data.email,
        company=company.name,
        )

@router.get('/management/')## after creating job  table 
def view_all_applications(db: Session = Depends(database.get_db), get_current_user : schemas.Admin = Depends(OAuth2.get_current_user)):
    if get_current_user.role != "admin":
        raise HTTPException(status_code=401, detail="unauthorized access")
    all_data = db.query(models.User).all()  
    return all_data

@router.delete('/management/{user_id}')
def delete_account(user_id : int, db: Session = Depends(database.get_db),get_current_user : schemas.Admin = Depends(OAuth2.get_current_user)):

    if get_current_user.role != "admin":
        raise HTTPException(status_code=401, detail="unauthorized access")
    
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {f"successfully deleted the user {user_id}"}

@router.patch('/management/{user_id}')
def update_email_or_password(user_id: int, request : schemas.UserUpdate, db: Session = Depends(database.get_db), get_current_user : schemas.Admin = Depends(OAuth2.get_current_user)): 

    if get_current_user.role != "admin":
        raise HTTPException(status_code=401, detail="unauthorized access")
     
    user = db.query(models.User).filter(models.User.id == user_id).first()
    user.email = request.email
    user.full_name = request.full_name 
    db.commit()
    db.refresh(user)
    return user    

@router.post("/createjob")
def create_job(request : schemas.JobPost, db : Session = Depends(database.get_db),get_current_user : schemas.TokenData = Depends(OAuth2.get_current_user)):

    if get_current_user.role != 'admin':
        raise HTTPException(status_code=401, detail="only company admin can post new job")
    new_job = models.Job(
        title = request.title,
        description = request.description,
        position = request.position
    )
    
    company = db.query(models.Company).filter(models.Company.admin_id == get_current_user.id).first()

    new_job.company_id = company.id
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return { f" {new_job.title} successfully added"}
    









