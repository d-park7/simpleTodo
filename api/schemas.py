from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    username: str
    
    class Config:
        orm_mode = True

class UserCreate(User):
    password: str
    
class Todo(BaseModel):
    todo: str
    
    class Config:
        orm_mode = True

# not sure why they do this in the docs
# ig mostly for keeping the same convention
# of separating the base from the methods?
class TodoCreate(Todo):
    pass