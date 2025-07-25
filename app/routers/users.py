from fastapi import APIRouter, Depends
from .. import schemas, database, models
from sqlalchemy.orm import Session


router = APIRouter(prefix="/users")

@router.get("/",response_model = list[schemas.UserOut])
def get_all_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


@router.post("/")
def CreateUser(request : schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(email = request.email, password = request.password, full_name = request.full_name, is_active = request.is_active)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
