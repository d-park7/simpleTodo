from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from .. import schemas, models
from ..database import get_db


router = APIRouter()


def get_user_by_email(email: str, db: Session):
    return db.query(models.User).filter(models.User.email == email).first()

@router.post("/create_users/", response_description="Create a user", response_model=schemas.UserInDB)
def create_user(user: schemas.UserInDB, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/update_users/{id}", response_description="Update a user", response_model=schemas.User)
def update_user(user: schemas.User, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    updated_user = user_query.first()
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    user_query.update(user)    
    db.commit()
    return updated_user

@router.post("/delete_user/{id}", response_description="Delete a user by email")
def delete_user(id: int, db: Session = Depends(get_db)):
    query_user = db.query(models.User).filter(models.User.id == id)
    if not query_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    query_user.delete()
    db.commit()
    return query_user.first() 