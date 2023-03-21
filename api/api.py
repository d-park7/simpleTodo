from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .models import Base
from .database import get_db, engine
from .schemas import User, UserCreate, UserInDB, Todo 
from .routers import auth, crud_todo, crud_user

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(crud_user.router)

@app.get("/api/healthchecker")
def root():
    return {"message": "Health checker"}