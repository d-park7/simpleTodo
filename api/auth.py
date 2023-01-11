from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import models
import schemas
from database import SessionLocal

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO: MOST IMPORTANT RN
# CREATE AUTH AND HAVE IT SET SO THAT ONLY LOGGED IN USERS CAN POST TODOS

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)): 
    user_form = get_user(db, form_data.username)
    if not user_form:
        raise HTTPException(status_code=404, detail="Incorrect username or password")
    user = schemas.UserInDB(id=user_form.id, username=user_form.username, password=user_form.password)
    hased_password = form_data.password
    if not hased_password == user.password:
        raise HTTPException(status_code=404, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def fake_decode_token(db: Session, token):
    # no security provided
    # just for dev use
    user = get_user(db, token)
    return user
    
def get_current_user(token: str = Depends(oauth2_scheme)):
    current_user = fake_decode_token(get_db, token)
    if not current_user.is_active:
        raise HTTPException(status_code=404, detail="Incorrect username or password")
    return current_user