from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models
from .. import utils, OAuth2


router = APIRouter(prefix="/create", tags=["Create"])

@router.post("/create_user_account")
def Create_Account(request : schemas.User, db: Session = Depends(database.get_db)):
    hashed_password = utils.hashing.pwd_cxt.hash(request.password)
    new_user = models.User( email = request.email, password = hashed_password, full_name = request.full_name)
    new_user.is_admin = False
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/create_admin_account")
def Create_Account(request : schemas.createAdmin, db: Session = Depends(database.get_db)):
    hashed_password = utils.hashing.pwd_cxt.hash(request.password)
    new_user = models.Admin( email = request.email, password = hashed_password, full_name = request.name)
    new_user.is_admin = True
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/create_company")
def Create_company(request : schemas.Company, db : Session = Depends(database.get_db), get_current_user : schemas.TokenData = Depends(OAuth2.get_current_user)):
    if get_current_user.role != "admin":
        raise HTTPException(status_code=401, detail="only admin can create company")

    new_company = models.Company(
        name = request.name,
        motto = request.motto,
        admin_id = get_current_user.id
    )

    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return {"msg": "Company created", "company_id": new_company.id}

