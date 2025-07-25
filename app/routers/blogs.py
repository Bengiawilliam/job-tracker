from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from .. import database,schemas, models

router = APIRouter(
    prefix="/blogs",
    tags=['Blogs']
)

@router.post('/')
def create_blog(request : schemas.BlogCreate,db : Session = Depends(database.get_db)): 
    new_blog = models.Blog(title = request.title, body  = request.body, user_id = request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

