from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from ..schemas import UserCreate, User 
from ..database import get_db


router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    password = user.password
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user