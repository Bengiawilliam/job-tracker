from fastapi import APIRouter, Depends
from .. import schemas, database, models
from sqlalchemy.orm import Session
router = APIRouter()


@router.get("/users")
def All(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


@router.post("/users")
def CreateUser(request : schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(email = request.email, hashed_password = request.hashed_password, fullname = request.fullname, is_active = request.is_active)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
