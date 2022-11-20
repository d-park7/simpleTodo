from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    username: str
    
    class Config:
        orm_mode = True

class UserCreate(User):
    password: str