from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from ..schemas import User
from ..config import settings
from ..database import get_db


SECRET_KEY = settings.JWT_PRIVATE_KEY
ALGORITHM = settings.JWT_ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def get_user(username: str, db: Session = Depends(get_db)):
    return db.query(User).filter(User.username == username).first()

async def authenticate_user(email: str, password: str, db: Session = Depends(get_db)):
    user = await get_user(email, db)
    if not user:
        return False
    if verify_password(password, user["hashed_password"]):
        return user

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user
    
@router.get("users/me")
def read_user_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}